import matplotlib.pyplot as plt
import def_prog

file_name = "14620265261315_0.txt"

df = def_prog.load_data(file_name)

time = df["time"]
temperature = df["temperature"]
pulse = df["pulse"]

peaks, pulse_count, bpm = def_prog.calc_heart_rate(
    time, pulse, height=2.7, distance=5
)

average_temp = def_prog.calc_average_temperature(temperature)

print("ピーク数:", pulse_count)
print("脈拍数:", round(bpm, 1), "bpm")
print("平均気温:", round(average_temp, 2), "℃")

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(time, pulse, color="blue", label="Pulse")
ax1.plot(time.iloc[peaks], pulse.iloc[peaks], "ro", label="Peaks")

ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Pulse [V]", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()
ax2.plot(time, temperature, color="green", label="Temperature")

ax2.set_ylabel("Temperature [℃]", color="green")
ax2.tick_params(axis="y", labelcolor="green")

plt.title(
    f"Pulse and Temperature\n"
    f"Heart Rate: {bpm:.1f} bpm, Average Temp: {average_temp:.2f} ℃"
)

ax1.grid()
plt.show()
