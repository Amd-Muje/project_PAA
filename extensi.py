import random
import time
import matplotlib.pyplot as plt


def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]


def is_unique(array):
    return len(array) == len(set(array))


def measure_time(array):
    start_time = time.perf_counter()
    unique = is_unique(array)
    end_time = time.perf_counter()
    return unique, end_time - start_time

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
stambuk_last_3_digits = 123  
max_value = 250 - stambuk_last_3_digits
seed = 42


average_times = []
worst_times = []


with open("worst_avg.txt", "w") as file:
    file.write("n\tWorst Case (s)\tAverage Case (s)\n")

    for n in n_values:
        
        array = generate_array(n, max_value, seed)

        
        _, avg_time = measure_time(array)
        
        
        worst_case_array = [1] * n
        _, worst_time = measure_time(worst_case_array)

        
        average_times.append(avg_time)
        worst_times.append(worst_time)

        
        file.write(f"{n}\t{worst_time:.6f}\t{avg_time:.6f}\n")


plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_times, label="Worst Case", marker="o")
plt.plot(n_values, average_times, label="Average Case", marker="o")
plt.title("Performance Analysis of Unique Element Check")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.show()
plt.savefig("performance_analysis.jpg")  # Simpan dalam format JPG
plt.show()

