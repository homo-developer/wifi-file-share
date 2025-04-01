import http.server
import socketserver
import socket
import os
import sys
from urllib.parse import quote


def print_banner():
    banner = """
    ===================================================
          W I F I  F I L E  S H A R E  H O M O
    ---------------------------------------------------
    | Built by: homo_developer | Powered by: rathell    |
    | Stealth Mode: ON  | Access: Unrestricted        |
    ---------------------------------------------------
    | Enter the file path, pick a port, and dominate!  |
    ===================================================
    """
    print(banner)


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def start_file_share():
    print_banner()
    
    
    file_path = input("Enter the full path of the file to share: ").strip()
    if not os.path.exists(file_path):
        print("That path doesn’t exist, mate. Check it and try again.")
        sys.exit(1)
    
    
    while True:
        try:
            port = int(input("Enter the port number (e.g., 8080): ").strip())
            if 1024 <= port <= 65535:
                break
            else:
                print("Port needs to be between 1024 and 65535. Try again.")
        except ValueError:
            print("That’s not a valid number, chief. Give me digits.")
    
    
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    os.chdir(file_dir)
    
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    
    
    local_ip = get_local_ip()
    encoded_file_name = quote(file_name)
    access_link = f"http://{local_ip}:{port}/{encoded_file_name}"
    
    print(f"\nFile server running, mate. Access it here: {access_link}")
    print("Share that link over WiFi, and they’ll grab the file.")
    print("Press Ctrl+C to shut it down when you’re done.")
    
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. Catch you later, boss!")
        httpd.server_close()

if __name__ == "__main__":
    start_file_share()