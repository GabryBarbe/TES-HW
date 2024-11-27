import scipy as sp
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(rate, data):
    # La durata è il numero di righe (campioni) diviso la frequenza di campionamento
    durata = data.shape[0] / rate
    
    plt.plot(np.linspace(0, durata, data.shape[0]), data)
    plt.xlabel("Tempo")
    plt.ylabel("Ampiezza")
    plt.grid(True)
    plt.show()  
    

def divisione_audio(rate, data, M):
    campioni_per_sezione = rate*M # numero di campioni per sezione
    num_sezioni = (len(data)//campioni_per_sezione) + 1# numero di sezioni
    
    sezioni = []
    for i in range(num_sezioni):
        inizio = i * campioni_per_sezione # inizio della sezione
        fine = (i+1) * campioni_per_sezione # fine della sezione
        sezioni.append(data[inizio:fine]) # aggiungo la szione 

    return sezioni

def plot_fft(freq, ampiezza, num_segmento):
    freq_pos = freq[freq > 0]
    ampiezza_pos = ampiezza[freq > 0]

    plt.plot(freq_pos, ampiezza_pos)
    plt.xlabel("Frequenza")
    plt.ylabel("Ampiezza")
    plt.suptitle("Segmento " + str(num_segmento))
    plt.grid(True)
    plt.show()

def calcolo_fft_libreria(rate, segmenti):
    for i,segmento in enumerate(segmenti):
        fft_segmento = sp.fft.fft(segmento)
        freq_segmento = sp.fft.fftfreq(len(segmento), d=1/rate)
        ampiezza_segmento = np.abs(fft_segmento)
        plot_fft(freq_segmento, ampiezza_segmento, i+1)
        

def main():
    # rate è la frequenza di campionamento
    # data è una matrice di 2 colonne (perchè il file è stereo) e tante 
    # righe quante sono i campioni
    # data.shape() restituisce il numero di righe e colonne della matrice

    rate, data = sp.io.wavfile.read("halleluja.wav")
    
    # sd.play(data, rate)  # riproduce il file audio
    # sd.wait() # attende la fine esecuzione del file audio
    
    sezioni = divisione_audio(rate, data, 15)

    # riproduzione dei segmenti di M secondi
    # for i in range(len(segmenti)):
    #     sd.play(segmenti[i], rate)
    #     sd.wait()   

    #plot_waveform(rate, data)

    calcolo_fft_libreria(rate, sezioni)

    return 0



main()
