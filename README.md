
# Project Title

A brief description of what this project does and who it's for


# IoT Bird Species Identification and Motion Alert Using ESP32-CAM and CNN MobileNet V2 Achitecture

A brief description of what this project does and who it's for


## Setup
Git clone

```bash
  git clone https://github.com/sanjay7178/iot-esp32-cam.git
  cd iot-esp32-cam
  
```
Import DB

```bash
   mysql -p -u root test < users.sql 
  
```    
## Installation

Installation of MySql db and few other python Libraries in Ubuntu 22.04 server

```bash
  sudo apt-get update && apt-get upgrade
  sudo apt-get install libmysqlclient-dev -y
  sudo apt install mysql-server -y
  sudo apt-get -y install python3-pip
  pip3 install flask-mysqldb -y
  pip3 install -r requirements.txt
```

## Deployment

To deploy this project run

```bash
  #python flask library must be isntalled 
  #for deployment flask Web and Rest API in deployment stage
  python3 -m Login.py --host='0.0.0.0'
```

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Authors

- [@Aniruth7171](https://www.github.com/Aniruth7171)
- [@KarnamShyam1947](https://www.github.com/KarnamShyam1947)
- [@sanjay7178](https://www.github.com/sanjay7178)

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/image.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-11-18%2023-53-01.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-11-18%2023-53-12.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-11-18%2023-52-48.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/8dc94c59-771c-4176-b243-9ec0b48d8324.jpg)

## circuit

![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-10-15%2011-59-52.png)

PIR Sensor,
TTL 3.3v/5v usb adapter,
Jumper Wires,
ESP32-CAM Board
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/0a2ca28c-90a2-4d26-8b42-c194b4d25bc9.jpg)

![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/7e8fd48d-09e0-4a4b-bb0e-2096944af307.jpg)
