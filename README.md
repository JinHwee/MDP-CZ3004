# Client-Server for Image recognition (NTU - MDP CZ/CE3004)

This repository consist of 2 types of backend files, written in bash and in python.

### Instructions here are for both scripts (python on Windows or bash in Linux)

#### Directory set up

Desktop -
        |- MDP-images -
                        |- raw_images (directory to store raw_images)
                        |- results (directory to store results)
                        |- venv (virtual environment)
                        |- yolov5 (git clone git@github.com:ultralytics/yolov5.git)
                        |- best.pt (model)


#### Modification to detect.py line 87

```python
save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)              # original 

save_dir = Path("<add your own directory to Desktop>\\MDP-images\\results")     # changed
```

#### Virtual environment set up
```python
python -m venv venv
# activate your virtual environment using venv/Scripts/activate, .ps1 for powershell, .bat for command prompt
# change directory to yolov5
cd yolov5

# install requirements for yolov5
pip install -r requirements.txt 


# install additional libraries for SSH and SCP
pip install paramiko scp
```

### Requires the following software packages (OS: Ubuntu 20.04)
Refer to automate_file_transfer.sh for more information

```bash
# Interactive password input from script
sudo apt install -y sshpass

# Changing the file to be executable
chmod +x automate_file_transfer.sh
```

Image recognition done via YOLOv5, custom model not uploaded.
Laptop must be connected to the AP on RPi for secure copy protocol (SCP) to work.

### Instructions from here on are for Windows 10 machines
Refer to python_automated_transfer.py for more information

```python
# for statements where < ... > are present, please modify accordingly
rawfiledir = "<add your own directory to Desktop>\\MDP-images\\raw_images\\"

# Also, you need to modify this statement to factor in the RPi IP address
ip = "<change to your own RPi ip>"
```