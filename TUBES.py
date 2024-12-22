import time

def fibonacci_rekurisif(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rekurisif(n - 1) + fibonacci_rekurisif(n - 2)

def fibonacci_iteratif(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def main():
    while True:
        print("\nPilih metode Fibonacci:")
        print("1. Rekursif")
        print("2. Iteratif")
        print("3. Keluar")
        
        choice = int(input("Masukkan pilihan : "))
        
        if choice == 3:
            print("Program selesai")
            break
        
        n = int(input("Masukkan angka n: "))
        
        if choice == 1:
            start_time = time.time()
            result = fibonacci_rekurisif(n)
            end_time = time.time()
            print(f"Fibonacci (rekursif) untuk n = {n} adalah {result}")
            print(f"Waktu eksekusi: {end_time - start_time:.100f} detik")
        elif choice == 2:
            start_time = time.time()
            result = fibonacci_iteratif(n)
            end_time = time.time()
            print(f"Fibonacci (iteratif) untuk n = {n} adalah {result}")
            print(f"Waktu eksekusi: {end_time - start_time:.100f} detik")
        else:
            print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
        
if __name__ == "__main__":
    main()
