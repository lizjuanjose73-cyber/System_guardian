import monitor
import evaluator
import logger
import config
import time

while True:
    info = monitor.obtener_info()
    cpu = monitor.obtener_cpu()
    ram = monitor.obtener_ram()

    estado = evaluator.evaluar(cpu, ram)

    print("Sistema:", info.system)
    print("CPU:", cpu)
    print("RAM:", ram.percent)
    print("Estado:", estado)
    print("----------------------")

    logger.guardar_log(cpu, ram, estado, config.LOG_FILE)

    time.sleep(3)
