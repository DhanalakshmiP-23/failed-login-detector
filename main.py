import re
from collections import Counter

LOG_FILE = "sample_log.txt"
THRESHOLD = 3  # flag an IP after this many failed logins

def read_failed_logins(path):
    """Return a list of IPs that had a failed login."""
    ips = []
    pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")
    with open(path) as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ips.append(match.group(1))
    return ips

def main():
    ips = read_failed_logins(LOG_FILE)
    counts = Counter(ips)

    print(f"Total failed logins: {len(ips)}\n")
    print("IP address        Failures   Status")
    print("-" * 40)
    for ip, n in counts.most_common():
        status = "SUSPICIOUS" if n >= THRESHOLD else "ok"
        print(f"{ip:<17} {n:<10} {status}")

if __name__ == "__main__":
    main()