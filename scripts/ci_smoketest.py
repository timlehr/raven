"""Temporary CI diagnostic: inspect the installed wheel and run the binary."""
import os
import subprocess
import sys

import otio_raven

bin_dir = os.path.join(os.path.dirname(otio_raven.__file__), "bin")
print("bin dir:", bin_dir)
print("contents:", os.listdir(bin_dir))

exe = os.path.join(bin_dir, "raven.exe" if os.name == "nt" else "raven")
print("exe:", exe, "exists:", os.path.exists(exe))

r = subprocess.run([exe, "--version"], capture_output=True, text=True)
print("returncode:", r.returncode)
print("stdout:", repr(r.stdout))
print("stderr:", repr(r.stderr))
sys.exit(r.returncode)
