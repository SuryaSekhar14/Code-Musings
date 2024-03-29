import psutil
import time

# while True:
#     print(psutil.cpu_percent())
#     print(psutil.virtual_memory().percent)
#     time.sleep(1)

def displayUsage(cpu_usage, mem_usage, bars=50):
    """
    Displays the CPU and memory usage in a progress bar format.

    Parameters:
    cpu_usage (float): The CPU usage percentage.
    mem_usage (float): The memory usage percentage.
    bars (int): The number of bars in the progress bar (default is 50).

    Returns:
    None
    """

    cpu_percentage = cpu_usage / 100.0
    mem_percentage = mem_usage / 100.0

    cpu_bar = '█' * int(cpu_percentage * bars) + '-' * (bars - int(cpu_percentage * bars))
    mem_bar = '█' * int(mem_percentage * bars) + '-' * (bars - int(mem_percentage * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end="")


while True:
    displayUsage(psutil.cpu_percent(), psutil.virtual_memory().percent)
    time.sleep(0.5)
















