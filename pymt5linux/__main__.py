import argparse
import shutil
from pathlib import Path
from subprocess import Popen
from rpyc.utils.classic import DEFAULT_SERVER_PORT, DEFAULT_SERVER_SSL_PORT
from pymt5linux import server
import os


def main():
    parser = argparse.ArgumentParser(description="Create Server.")
    parser.add_argument(
        "--python",
        type=str,
        help="Python that will run the server (have to be a Windows version!)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="The host to connect to. The default is localhost"
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=DEFAULT_SERVER_PORT,
        help=f"The TCP listener port (default = {DEFAULT_SERVER_PORT!r}, default for SSL = {DEFAULT_SERVER_SSL_PORT!r})"
    )
    parser.add_argument(
        '-w',
        '--wine',
        type=str,
        default='wine',
        help='Command line to call wine program (default = wine)',
        )
    parser.add_argument(
        "-s",
        "--server",
        type=str,
        default="tmp/pymt5linux",
        help="Path where the server will be build and run (default = /tmp/pymt5linux)"
    )

    args = parser.parse_args()
    os.makedirs(args.server, exist_ok=True)

    # Generate server script
    server_script_path = os.path.join(args.server, 'server.py')
    shutil.copy2(src=server.__file__, dst=server_script_path)

    # Start the server
    cmd = [
        args.wine,
        args.python,
        server_script_path,
        '--host',
        str(args.host),
        '-p',
        str(args.port)
    ]
    Popen(cmd).wait()


if __name__ == "__main__":
    main()