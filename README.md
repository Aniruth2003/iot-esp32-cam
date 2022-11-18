
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

- [@Aniruth](https://www.github.com/)
- [@Shyam](https://www.github.com/)
- [@sanjay7178](https://www.github.com/sanjay7178)

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/image.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-11-18%2023-53-01.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-11-18%2023-53-12.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/Screenshot%20from%202022-11-18%2023-52-48.png)
![App Screenshot](https://raw.githubusercontent.com/sanjay7178/iot-esp32-cam/main/screenshots/8dc94c59-771c-4176-b243-9ec0b48d8324.jpg)
