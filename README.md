# python_ssh_exe
pythonベースのssh先でコマンド実行するコードのexe化

```
usage: main.py [-h] --hostname HOSTNAME --user USER [--password PASSWORD] [-i IDENTITY_FILE] [-p PORT] -c COMMAND

optional arguments:
  -h, --help            show this help message and exit
  --hostname HOSTNAME   hostname
  --user USER           user
  --password PASSWORD   password
  -i IDENTITY_FILE, --identity_file IDENTITY_FILE
                        identity file
  -p PORT, --port PORT  port
  -c COMMAND, --command COMMAND
                        command
```

## 開発用
**linux向けコマンド**

```
docker build  -f ./linux/Dockerfile -t python-ssh-exe-linux .
docker run --rm -it python-ssh-exe-linux bash

docker run --rm -v $(pwd)/src:/src -v $(pwd)/linux:/linux \
    python-ssh-exe-linux pyinstaller main.py \
    --onedir --onefile --clean \
    --distpath /linux/dist \
    --workpath /linux/build \
    --specpath /linux 
```

**centos7向けコマンド**

```
docker build  -f ./centos7/Dockerfile -t python-ssh-exe-centos7 .
docker run --rm -it python-ssh-exe-centos7 bash

docker run --rm -v $(pwd)/src:/src -v $(pwd)/centos7:/centos7 \
    python-ssh-exe-centos7 pyinstaller main.py \
    --onedir --onefile --clean \
    --distpath /centos7/dist \
    --workpath /centos7/build \
    --specpath /centos7 
```

**windows向けコマンド**

```

```