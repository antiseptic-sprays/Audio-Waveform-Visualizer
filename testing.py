import sounddevice as sd
import numpy as np

# Find loopback device index
devices = sd.query_devices()
loopback_device = None
for i, d in enumerate(devices):
    if "loopback" in d['name'].lower():
        loopback_device = i
        break

if loopback_device is None:
    raise RuntimeError("No WASAPI loopback device found. Enable Stereo Mix or VB-Cable.")

def callback(indata, frames, time, status):
    amplitude = np.linalg.norm(indata) * 10
    bar = "#" * int(amplitude)
    print(bar)

with sd.InputStream(device=loopback_device, channels=2, samplerate=44100, callback=callback):
    print("Capturing system audio. Ctrl+C to stop.")
    while True:
        sd.sleep(100)