#!/bin/bash

while :
do

clear

echo 


echo
echo -e "\033[32m                                ███████╗ █████╗ ██╗  ██╗███████╗ █████╗ ██████╗     \033[0m"
echo -e "\033[32m                                ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔══██╗    \033[0m"
echo -e "\033[32m                                █████╗  ███████║█████╔╝ █████╗  ███████║██████╔╝    \033[0m"
echo -e "\033[32m                                ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██║██╔═══╝     \033[0m"
echo -e "\033[32m                                ██║     ██║  ██║██║  ██╗███████╗██║  ██║██║         \033[0m"
echo -e "\033[32m                                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝         \033[0m"
echo                                                
echo -e "\033[32m                                          https://github.com/bl4ck44                \033[0m"

echo

int_handler (){
    clear
    echo
    echo "[+] Adios"
    kill $PPID
    exit 1
}

trap 'int_handler' INT

if [ "$(id -u)" != "0" ]; then
   echo "Ejecute este script como root (usando sudo)."
   exit 1
fi

echo

echo -e "\033[1m [1] Instalar requisitos \033[0m"
echo -e "\033[1m [2] Configurar FakeAP \033[0m"
echo -e "\033[1m [3] Reiniciar la red y el sistema \033[0m"
echo -e "\033[1m [4] Salir \033[0m"

echo

#leemos del teclado
read -p $'\033[1m [+] Seleccione una opción: \033[0m' opcion

Ventanas(){
        for t in {0..1}
        do
            xterm &
        done
}

nombre(){
       echo -e "\033[1m Ingresa el nombre la red wifi nueva:\033[0m"
       read nombre
       sed -i "s|ssid=|ssid=$nombre|g" hostapd.conf
}

password(){
       echo -e "\033[1m Ingresa la contraseña:\033[0m"
       read password
       sed -i "s|wpa_passphrase=|wpa_passphrase=$password|g" hostapd.conf
}

ubicacion(){
       # Preguntar al usuario la nueva ubicación
       echo -e "\033[1m Ingresa la ubicación para guardar el historial:\033[0m"
       read nueva_ubicacion
       # Editar el archivo y reemplazar la ubicación anterior
       sed -i "s|log-facility=/home/usuario/Hacking/Scripts/Hacking Wifi/FackeAP/dnsmasq.log|$nueva_ubicacion/dnsmasq.log|g" dnsmasq.conf
}

case $opcion in
        1) echo 
        echo "\033[1m [+] Instalando \033[0m"
        echo
        sudo apt-get install hostapd dnsmasq
        echo
        echo "[+] Requisistos instalados"
        sleep 1.5;;

        2) echo
        nombre
        password
        ubicacion
        airmon-ng start wlan0
        ifconfig wlan0 up 192.168.1.1 netmask 255.255.255.0
        route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1 
        iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
        iptables --append FORWARD --in-interface wlan0 -j ACCEPT
        echo 1 > /proc/sys/net/ipv4/ip_forward
        Ventanas
        sleep 1.5;;

        3) echo
        echo "[+] Reiniciando la red y el sistema"
        echo
        sudo systemctl restart NetworkManager.service
        reboot
        sleep 1.5;;

        4) echo
        exit;;

        *) echo "Opción incorrecta";;
esac

echo

done