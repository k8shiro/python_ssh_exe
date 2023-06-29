from argparse import ArgumentParser
import paramiko
import json


def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('--hostname', type=str, required=True,
                           help='hostname')
    argparser.add_argument('--user', type=str, required=True,
                           help='user')
    argparser.add_argument('--password', type=str,
                           help='password')
    argparser.add_argument('-i', '--identity_file', type=str,
                           help='identity file')
    argparser.add_argument('-p', '--port', type=int,
                           default=22,
                           help='port')
    argparser.add_argument('-c', '--command', type=str, required=True,
                        help='command')
    return argparser.parse_args()

def ssh(hostname, user, password, identity_file, port, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if identity_file:
            client.connect(hostname, username=user, key_filename=identity_file)
        elif password:
            client.connect(hostname, username=user, password=password)
        else:
            client.connect(hostname, username=user)

        stdin, stdout, stderr = client.exec_command(command)
        stdout, stderr = stdout.read().decode(), stderr.read().decode()
    except:
        client.close()
        raise
    finally:
        client.close()
    return stdout, stderr

def main():
    args = get_option()
    hostname = args.hostname
    user = args.user
    password = args.password
    identity_file = args.identity_file
    port = args.port
    command = args.command

    stdout, stderr = ssh(hostname, user, password, identity_file, port, command)

    data = {
        "stdout": stdout,
        "stderr": stderr,
    }
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()