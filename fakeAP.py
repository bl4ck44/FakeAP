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
        os.system("\nairmon-ng start wlan0")
        os.system("ifconfig wlan0 up 192.168.1.1 netmask 255.255.255.0")
        os.system("route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1")
        os.system("iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE")
        os.system("iptables --append FORWARD --in-interface wlan0 -j ACCEPT")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward\n") 
        subprocess.Popen(['xterm', '-e', 'bash', '-c', 'hostapd hostapd.conf; exec bash']) 
        subprocess.Popen(['xterm', '-e', 'bash', '-c', 'dnsmasq -C dnsmasq.conf -d; exec bash'])
    elif opcion == "3":
        print("\033[1m\n[+] Reiniciando la red y el sistema\n \033[0m")
        os.system("sudo systemctl restart NetworkManager.service")
    elif opcion == "4":
        # Salir del programa
        break
    else:
        print("Opción inválida")
