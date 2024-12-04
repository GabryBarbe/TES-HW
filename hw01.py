import scipy as sp
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(rate, data):
    """
    Plot della waveform del segnale audio

    Args:
        rate: frequenza di campionamento del segnale audio
        data: contenuto del segnale audio
    """
    # La durata è il numero di righe (campioni) diviso la frequenza di campionamento
    durata = data.shape[0] / rate
    
    plt.plot(np.linspace(0, durata, data.shape[0]), data)
    plt.xlabel("Tempo")
    plt.ylabel("Ampiezza")
    plt.grid(True)
    plt.show()  

def divisione_audio(rate, data, M):
    """
    Divisione del segnale audio in sezioni di M secondi

    Args:
        rate: frequenza di campionamento del segnale audio 
        data: contenuto del segnale audio
        M (integer): durata in secondi di ogni sezione

    Returns:
        sezioni (list): lista di sezioni di M secondi
    """
    campioni_per_sezione = rate*M # numero di campioni per sezione
    num_sezioni = (data.shape[0]//campioni_per_sezione) + 1# numero di sezioni
    
    sezioni = []
    for i in range(num_sezioni):
        inizio = i * campioni_per_sezione # inizio della sezione
        fine = (i+1) * campioni_per_sezione # fine della sezione
        sezioni.append(data[inizio:fine]) # aggiungo la sezione 

    return sezioni

def plot_fft(freq, ampiezza, num_segmento):
    """
    Plot della FFT del segnale audio

    Args:
        freq: frequenze della FFT
        ampiezza: ampiezze della FFT
        num_segmento (integer): numero del segmento
    """
    # seleziono solo le frequenze e ampiezze positive
    freq_pos = [0.5 + f for f in freq]
    ampiezza_pos = np.concatenate((ampiezza[len(ampiezza)//2 : ],ampiezza[0 : len(ampiezza)//2]))
    plt.plot(freq_pos, ampiezza_pos)
    plt.xlabel("Frequenza")
    plt.ylabel("Ampiezza")
    plt.suptitle("Segmento " + str(num_segmento))
    plt.grid(True)
    plt.show()

def calcolo_fft_libreria(segmenti):
    """
    Calcolo della FFT del segnale audio con la libreria scipy

    Args:
        segmenti (list): lista di sezioni di M secondi
    """
    for i,segmento in enumerate(segmenti):
        fft_segmento = sp.fft.fft(segmento) #calcolo fft del segmento
        freq_segmento = sp.fft.fftfreq(len(segmento)) #calcolo frequenze 
        ampiezza_segmento = np.abs(fft_segmento) #calcolo ampiezze
        plot_fft(freq_segmento, ampiezza_segmento, i+1)
        
def calcolo_dft_manuale(segmenti):
    """
    Calcolo della DFT 
    
    Args:
        segmenti (list): lista di sezioni di M secondi
    """
    for i,segmento in enumerate(segmenti):
        N = len(segmento)
        X = np.zeros(N, dtype=complex)
        for k in range(N):
            for n in range(N):
                X[k] += segmento[n] * np.exp(-2j*np.pi*k*n/N)
        freq = np.linspace(0, 0.5, N//2)
        ampiezza = np.abs(X[:N//2])
        plot_fft(freq, ampiezza, i+1)


def main():
    # rate è la frequenza di campionamento
    # data è una matrice di 2 colonne (perchè il file è stereo) e tante 
    # righe quante sono i campioni
    # data.shape() restituisce il numero di righe e colonne della matrice
    
    rate, data = sp.io.wavfile.read("halleluja.wav")
    data = data[:,0] # prendo solo una colonna
    
    # sd.play(data, rate)  # riproduce il file audio
    # sd.wait() # attende la fine esecuzione del file audio
    
    sezioni = divisione_audio(rate, data, 1)

    # riproduzione dei segmenti di M secondi
    # for i in range(len(sezioni)):
    #     sd.play(sezioni[i], rate)
    #     sd.wait()   

    plot_waveform(rate, data)

    calcolo_dft_manuale(sezioni)

    return 0

main()
