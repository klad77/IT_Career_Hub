import cowsay
import platform

system_info = f"System: {platform.system()}\n" \
              f"Node Name: {platform.node()}\n" \
              f"Release: {platform.release()}\n" \
              f"Version: {platform.version()}\n" \
              f"Machine: {platform.machine()}\n" \
              f"Processor: {platform.processor()}"

cowsay.cow(system_info)
