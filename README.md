# Read temperature and humidity with DHT sensors
![](https://i.imgur.com/8kgWJW8.png)

Medir temperatura y humedad del ambiente usando sensores de temperatura DHT, Arduino y Python

## Requisitos

### En arduino

#### Instalar [FirmataExpress](https://github.com/MrYsLab/FirmataExpress)
<details>
  <summary>En arduino-cli</summary>
  
```
arduino lib install --git-url https://github.com/MrYsLab/FirmataExpress.git
```

> Es necesario tener activa la opción `enable_unsafe_install` del archivo de [configuración de Arduino-cli](https://arduino.github.io/arduino-cli/0.20/configuration/)

</details>
<details>
  <summary>En arduino IDE</summary>

https://mryslab.github.io/pymata4/firmata_express/#installation-instructions
  
</details>

#### Cargar el [proyecto de FirmataExpress](https://github.com/MrYsLab/FirmataExpress) a la placa de Arduino

### Librerías de Python

- PySide6
- matplotlib
- pymata4

```bash
pip install -r requirements.txt
```

### Material usado
- Placa de Arduino MEGA 2560
- Sensor DHT11

## Características
- Mostrar la humedad (%) y la temperatura en (°C y °F) dentro de labels.
- Graficar la temperatura.

### En proceso

> [!TIP]
>
> Graficar la humedad.
