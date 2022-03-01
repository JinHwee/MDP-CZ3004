import os
import cv2
import sys
import time
import subprocess
import paramiko
from paramiko import SSHClient
from scp import SCPClient

sys.path.append("<add your own directory to Desktop>\\MDP-images\\venv\\lib\\site-packages")

rawfiledir = "<add your own directory to Desktop>\\MDP-images\\raw_images\\"
resultsdir = "<add your own directory to Desktop>\\MDP-images\\results\\"
ip = "<change to your own RPi ip>"

def transfer_file(name):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname=ip, username="pi", password="raspberry")
    scp = SCPClient(ssh.get_transport())
    scp.put(name, "/home/pi/Desktop/MDPGroup20/results/")
    scp.close()
    print("File %s has been sent..." % name)

def perform_image_rec():
    # sys.argv[0] == python_automated_transfer.py
    # just pass in numbers, brute forcing image name to be testx.jpg, where x in [1, N] and N is the number of obstacles
    # brute forcing label name to be testx.txt, where x is as mentioned
    images = sys.argv[1:]
    for index in images:
        imagename = "test%s.jpg" % index
        textname = "test%s.txt" % index
        files = [f for f in os.listdir(rawfiledir)]
        while imagename not in files:
            files = [f for f in os.listdir(rawfiledir)]
        subprocess.Popen(['<add your own directory to Desktop>/MDP-images/venv/Scripts/python.exe', '.\\detect.py', '--weights',
            '..\\best.pt', '--img', '544', '--conf', '0.25', '--source',
            '..\\raw_images/%s' % imagename, '--save-txt', '--project',
            '<add your own directory to Desktop>\\MDP-images\\results\\'
        ])
        time.sleep(10)
        labeldir = resultsdir + 'labels\\'
        txtfiles = [f for f in os.listdir(labeldir)]
        if textname not in txtfiles:
            textpath = labeldir + textname
            with open(textpath, 'w') as file:
                file.write("No labels detected\n")
                file.close()
        transfer_file(labeldir + textname)
    print("Done with all transfer")

if __name__ == "__main__":
    perform_image_rec()
