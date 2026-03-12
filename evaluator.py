def evaluar(cpu, ram):
    if cpu > 80 or ram.percent > 80:
        return "ALTO CONSUMO"
    else:
        return "NORMAL"
