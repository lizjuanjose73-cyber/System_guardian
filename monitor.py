import psutil
import platform

def obtener_info():
    return platform.uname()

def obtener_cpu():
    return psutil.cpu_percent(interval=1)

def obtener_ram():
    return psutil.virtual_memory()
