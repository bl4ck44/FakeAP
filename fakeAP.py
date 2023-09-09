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
    print("[+] Ejecute este script como root (usando sudo).\n")
    os.system("exit")



wifi = pywifi.PyWiFi()

# Obtiene la lista de adaptadores inalámbricos disponibles
interfaces = wifi.interfaces()

if len(interfaces) == 0:
    print("No se encontraron adaptadores inalámbricos disponibles.")
else:
    print("\033[1m\n[+] Adaptadores inalámbricos disponibles:\033[0m")

    # Almacena el nombre del primer adaptador en una variable
    primer_adaptador_nombre = interfaces[0].name()

    for i, iface in enumerate(interfaces, start=1):
        print(f"{i}. Nombre: {iface.name()}")



while True:                                                   
    print("\n\033[1m[1] Instalar requisitos\033[0m")
    print("\033[1m[2] Configurar FakeAP\033[0m")
    print("\033[1m[3] Reiniciar la red y el sistema\033[0m")
    print("\033[1m[4] Salir\033[0m")
    opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
    if opcion == "1":
        print("\033[1m\n[+] Instalando\n \033[0m")
        os.system("sudo apt-get install hostapd dnsmasq")
        print("\033[1m\n[+] Requisistos instalados\n \033[0m")
    elif opcion == "2":
        os.system(f"airmon-ng start {primer_adaptador_nombre}")
        os.system(f"ifconfig {primer_adaptador_nombre} up 192.168.1.1 netmask 255.255.255.0")
        os.system("route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1")
        os.system("iptables --table nat --append POSTROUTING --out-interface enp0s3 -j MASQUERADE")
        os.system(f"iptables --append FORWARD --in-interface {primer_adaptador_nombre} -j ACCEPT")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward\n")
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'hostapd hostapd.conf -i {primer_adaptador_nombre}; exec bash'])
        subprocess.Popen(['xterm', '-e', 'bash', '-c', f'dnsmasq -C dnsmasq.conf -d -i {primer_adaptador_nombre}; exec bash'])
    elif opcion == "3":
        print("\033[1m\n[+] Reiniciando la red y el sistema\n \033[0m")
        os.system("sudo systemctl restart NetworkManager.service")
    elif opcion == "4":
        # Salir del programa
        break
    else:
        print("Opción inválida")
