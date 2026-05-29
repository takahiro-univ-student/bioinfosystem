import pandas as pd
from scipy.signal import find_peaks

def load_data(file_name):
    df = pd.read_csv(file_name, sep=r"\s+", header=None)
    df.columns = ["time", "temperature", "pulse"]
    return df

def calc_heart_rate(time, pulse, height=2.7, distance=5):
    peaks, _ = find_peaks(pulse, height=height, distance=distance)
    measurement_time = time.iloc[-1] - time.iloc[0]
    pulse_count = len(peaks)
    bpm = pulse_count / measurement_time * 60
    return peaks, pulse_count, bpm

def calc_average_temperature(temperature):
    return temperature.mean()
