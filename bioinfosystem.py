import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

file_name = "14620265261315_0.txt"

df = pd.read_csv(file_name, sep=r"\s+", header=None)
df.columns = ["time", "temperature", "pulse"]

time = df["time"]
temperature = df["temperature"]
pulse = df["pulse"]

peaks, _ = find_peaks(pulse, height=2.7, distance=5)

measurement_time = time.iloc[-1] - time.iloc[0]
pulse_count = len(peaks)
bpm = pulse_count / measurement_time * 60

average_temp = temperature.mean()

print("ピーク数:", pulse_count)
print("脈拍数:", round(bpm, 1), "bpm")
print("平均気温:", round(average_temp, 2), "℃")


fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(time, pulse, color="blue", label="Pulse")
ax1.plot(time.iloc[peaks], pulse.iloc[peaks], "ro", label="Peaks")

ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Pulse [V]", color="blue")
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(time, temperature, color="green", label="Temperature")

ax2.set_ylabel("Temperature [℃]", color="green")
ax2.tick_params(axis='y', labelcolor='green')

plt.title(f"Pulse and Temperature\nHeart Rate: {bpm:.1f} bpm")

ax1.grid()

plt.show()