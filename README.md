# FakeAP

<p align="center">
<img src="Logotipo.png" width="278px">
</p>

Una Fake AP (Punto de Acceso Falso) es una red inalámbrica fraudulenta que se crea para engañar a los usuarios y hacerles creer que están conectados a una red y segura

Una vez que un usuario se conecta a la Fake AP, el hacker puede interceptar y registrar toda la información transmitida entre el usuario y la red, lo que puede poner en riesgo la privacidad y la seguridad de los datos del usuario.

<br>

```
git clone https://github.com/bl4ck44/FakeAP.git

cd FakeAP

chmod +x fakeAP.sh

sudo bash fakeAP.sh
```

<br>

![menú](Img/captura1.png)

Luego en las nuevas ventanas ejecutar los siguientes comandos:

```
hostapd.conf

dnsmasq -C dnsmasq.conf -d
```