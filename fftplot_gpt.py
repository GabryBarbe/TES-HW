import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Carica il file audio e calcola lo spettro
def plot_audio_spectrum(file_path):
    # Legge il file audio
    sample_rate, audio_data = wav.read(file_path)
    
    # Se il file è stereo, converte in mono
    if audio_data.ndim > 1:
        audio_data = audio_data.mean(axis=1)
    
    # Numero di campioni
    n = len(audio_data)
    
    # Calcola le frequenze e lo spettro tramite la FFT
    frequencies = np.fft.fftfreq(n, d=1/sample_rate)
    spectrum = np.abs(np.fft.fft(audio_data)) / n
    #print(frequencies[:10], spectrum[:10])
    #print(frequencies[len(frequencies)//2+1])
    # Calcola la risoluzione in frequenza
    delta_f = sample_rate / n
    #print(f"Risoluzione in frequenza (Delta f): {delta_f} Hz")
    print((audio_data)[:10])
    # Disegna il grafico dello spettro
    # plt.figure(figsize=(12, 6))
    # plt.plot(frequencies, spectrum, color='blue', lw=1)
    # plt.title("Spettro del segnale audio")
    # plt.xlabel("Frequenza (Hz)")
    # plt.ylabel("Ampiezza")
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()

# Percorso al file audio
file_path = "halleluja.wav"  # Sostituisci con il percorso del tuo file audio

# Esegui la funzione
plot_audio_spectrum(file_path)
