
import argparse
import ipaddress
import math
import socket
import time

from concurrent.futures import ThreadPoolExecutor


def parse_ports(value):
    """Parse individual ports and port ranges."""

    ports = set()

    try:
        for part in value.split(","):
            part = part.strip()

            if not part:
                raise ValueError

            if "-" in part:
                start, end = map(int, part.split("-", 1))

                if start > end:
                    raise ValueError

                if start < 1 or end > 65535:
                    raise ValueError

                ports.update(range(start, end + 1))

            else:
                port = int(part)

                if not 1 <= port <= 65535:
                    raise ValueError

                ports.add(port)

    except ValueError:
        raise argparse.ArgumentTypeError(
            "Invalid ports. Examples: 1-1024 or 22,80,443"
        )

    if not ports:
        raise argparse.ArgumentTypeError("No ports specified.")

    return sorted(ports)


def scan_port(target, port, timeout):
    """Test a TCP port and reject local self-connections."""

    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(timeout)

            result = sock.connect_ex((target, port))

            if result != 0:
                return None

            # Get local and remote socket endpoints.
            local_endpoint = sock.getsockname()
            remote_endpoint = sock.getpeername()

            # Prevent false positives caused by TCP self-connects.
            if local_endpoint == remote_endpoint:
                return None

            return port

    except OSError:
        return None


def get_service(port):
    """Return the conventional TCP service name."""

    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "Unknown"


def main():

    parser = argparse.ArgumentParser(
        description="PyRecon - Python TCP Port Scanner"
    )

    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target IPv4 address or hostname"
    )

    parser.add_argument(
        "-p", "--ports",
        type=parse_ports,
        default=parse_ports("1-65535"),
        help="Port range or individual ports (default: 1-65535)"
    )

    parser.add_argument(
        "-T", "--timeout",
        type=float,
        default=0.5,
        help="Connection timeout in seconds (default: 0.5)"
    )

    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=100,
        help="Maximum concurrent workers (default: 100)"
    )

    args = parser.parse_args()

    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("Timeout must be a positive finite number.")

    if not 1 <= args.workers <= 1000:
        parser.error("Workers must be between 1 and 1000.")

    # Resolve target address.
    try:
        target = socket.gethostbyname(args.target)
        ipaddress.IPv4Address(target)

    except (socket.gaierror, ValueError):
        parser.error("Invalid target IP address or hostname.")

    ports = args.ports
    total_ports = len(ports)

    print("\n" + "=" * 60)
    print("                 PYRECON v1.2.0")
    print("                 TCP PORT SCANNER")
    print("=" * 60)

    print(f"Target       : {target}")
    print(f"Ports        : {total_ports}")
    print(f"Workers      : {args.workers}")
    print(f"Timeout      : {args.timeout}s")
    print("=" * 60)

    open_ports = []
    completed = 0

    start_time = time.perf_counter()

    try:
        with ThreadPoolExecutor(
            max_workers=args.workers
        ) as executor:

            batch_size = 1000

            for i in range(0, total_ports, batch_size):

                batch = ports[i:i + batch_size]

                results = executor.map(
                    lambda port: scan_port(
                        target,
                        port,
                        args.timeout
                    ),
                    batch
                )

                for result in results:

                    completed += 1

                    if result is not None:
                        open_ports.append(result)

                print(
                    f"\rProgress: {completed}/{total_ports}",
                    end="",
                    flush=True
                )

    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted.")

    elapsed = time.perf_counter() - start_time

    print("\n\n" + "=" * 60)
    print("                  SCAN RESULTS")
    print("=" * 60)

    if open_ports:

        for port in sorted(open_ports):

            service = get_service(port)

            print(
                f"[+] {port:<7} OPEN | Service: {service}"
            )

    else:
        print("No open TCP ports found.")

    print("-" * 60)
    print(f"Open ports     : {len(open_ports)}")
    print(f"Ports checked  : {completed}/{total_ports}")
    print(f"Duration       : {elapsed:.2f} seconds")
    print("=" * 60)


if __name__ == "__main__":
    main()
