from datetime import datetime

def guardar_log(cpu, ram, estado, archivo):
    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(archivo, "a") as f:
        f.write(f"{tiempo} | CPU:{cpu}% RAM:{ram.percent}% Estado:{estado}\n")
