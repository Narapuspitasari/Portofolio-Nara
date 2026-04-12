# win_wifi.py — requires running as a user that can access saved profiles
import subprocess
import shlex

def get_profiles():
    out = subprocess.check_output(shlex.split("netsh wlan show profiles"), text=True, errors='ignore')
    profiles = []
    for line in out.splitlines():
        if "All User Profile" in line or "Profil Semua Pengguna" in line:
            # handle localized output by splitting on ':' and stripping
            parts = line.split(":")
            if len(parts) >= 2:
                profiles.append(parts[1].strip())
    return profiles

def get_password(profile):
    cmd = f'netsh wlan show profile name="{ }" key=clear'
    out = subprocess.check_output(cmd, shell=True, text=True, errors='ignore')
    for line in out.splitlines():
        if "Key Content" in line or "Konten Kunci" in line:
            return line.split(":")[1].strip()
    return None

if __name__ == "__main__":
    for p in get_profiles():
        print(f"{p} -> {get_password(p)}")
