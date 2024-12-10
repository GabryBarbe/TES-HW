import matplotlib.pyplot as plt

def main():
    plt.figure(figsize=(12, 6))
    plt.plot([1, 2, 3, -3, -2, -1], [1, 2, 3, 4, 5, 6], color='blue', lw=1)
    plt.title("Spettro del segnale audio")
    plt.xlabel("Frequenza (Hz)")
    plt.ylabel("Ampiezza")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

main()