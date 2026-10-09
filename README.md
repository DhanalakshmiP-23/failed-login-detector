# Failed Login Detector

Small Python script that reads an SSH auth log and flags IPs with repeated failed logins (basic brute-force detection).

## How it works
- Reads `sample_log.txt`
- Uses regex to pull the IP from "Failed password" lines
- Counts failures per IP
- Flags any IP with 3+ failures as SUSPICIOUS

## Run
```
python main.py
```

## Sample output
```
Total failed logins: 8

IP address        Failures   Status
----------------------------------------
192.168.1.50      4          SUSPICIOUS
203.0.113.9       3          SUSPICIOUS
198.51.100.7      1          ok
```

## Ideas to extend
- Take log file path as a command-line argument
- Export results to CSV
- Add time-window detection (e.g. 5 failures in 1 minute)