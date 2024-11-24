import subprocess
import tarfile
import urllib.request
import os
import json

file_name = 'xmrig-6.22.2-linux-static-x64.tar.gz'
extracted_folder = 'xmrig-6.22.2'
config_path = f'{extracted_folder}/config.json'

if not os.path.exists(extracted_folder):
    print("Downloading and extracting XMRig...")
    urllib.request.urlretrieve(
        'https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz', 
        file_name
    )
    with tarfile.open(file_name, 'r:gz') as tar:
        tar.extractall()
    os.remove(file_name)

config_data = {
    "api": {
        "id": None,
        "worker-id": "server1"
    },
    "http": {
        "enabled": False,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": None,
        "restricted": True
    },
    "autosave": True,
    "background": False,
    "colors": True,
    "title": True,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": True,
        "rdmsr": True,
        "wrmsr": True,
        "cache_qos": False,
        "numa": True,
        "scratchpad_prefetch_mode": 2
    },
    "cpu": {
        "enabled": True,
        "huge-pages": True,
        "huge-pages-jit": False,
        "hw-aes": None,
        "priority": 5,
        "memory-pool": False,
        "yield": True,
        "max-threads-hint": 100,
        "asm": True,
        "argon2-impl": None,
        "cn/0": False,
        "cn-lite/0": False,
        "threads": 23
    },
    "log-file": None,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "gr",
            "coin": "GR",
            "url": "eu.flockpool.com:5555",
            "user": "RGeuFkeSsQWhgJqvj1S7xnLGW9Mmgu5fgm",
            "pass": "x",
            "rig-id": "server1",
            "nicehash": False,
            "keepalive": True,
            "enabled": True,
            "tls": True,
            "tls-fingerprint": None,
            "daemon": False,
            "socks5": None,
            "self-select": None,
            "submit-to-origin": False
        }
    ],
    "print-time": 30,
    "health-print-time": 60,
    "dmi": True,
    "retries": 5,
    "retry-pause": 5,
    "syslog": False,
    "tls": {
        "enabled": False,
        "protocols": None,
        "cert": None,
        "cert_key": None,
        "ciphers": None,
        "ciphersuites": None,
        "dhparam": None
    },
    "dns": {
        "ipv6": False,
        "ttl": 30
    },
    "user-agent": None,
    "verbose": 0,
    "watch": True,
    "pause-on-battery": False,
    "pause-on-active": False
}

print("Updating config.json...")
with open(config_path, 'w') as config_file:
    json.dump(config_data, config_file, indent=4)

print("Starting XMRig...")
subprocess.run(f'./{extracted_folder}/xmrig'.split(), shell=True)
