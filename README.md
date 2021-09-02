# IIT-M Netaccess

## This is a repository for the script automating IIT-M Netaccess.

### Files

- `netaccess.py`

This is the *python script* file for the website blocker.

- `netaccess.service`

This is the *unit file* for running the python script as a system service and loading it at startup.

### Installation Instructions

- Download the repository by executing following commands

```
cd ~/Downloads
git clone https://github.com/ornkkk/IIT-M-Netaccess.git
cd IIT-M-Netaccess
```

- Open the `netaccess.py` file and edit the following lines.

~~~
user = "Roll Number" #Replace with your roll number
pwd = "Password" #Replace with your password
~~~

- Change the `user`, `pwd` accordingly.
- Open `netaccess.service` and add the absolute path to the python script file to `ExecStart` parameter. By default the absolute path is `/home/<user>/Downloads/IIT-M-Netaccess/netaccess.py`

  ~~~
  ExecStart=/home/<user>/Downloads/IIT-M-Netaccess/netaccess.py
  ~~~
  Note: Replace `<user>` with your username.
 
 - Give execute permissions to the script file
 ```
 sudo chmod +x netaccess.py
 ```
 - Add the unit file to the system services to automatically load at every startup
 ```
 sudo cp netaccess.service /etc/systemd/system/
 sudo systemctl daemon-reload
 reboot
 ```
 - After reboot you can see that the script file will be running automatically.

