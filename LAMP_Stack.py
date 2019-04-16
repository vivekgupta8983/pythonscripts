#!/bin/usr/python
import subprocess
def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Deploy LAMP Server")
    print("2. Do something else")
    print("3. Exit")
    print(67 * "-")

def deploy_httpd():
    commands_to_run = ['yum', '-y', 'install', 'httpd', 'mariadb', 'mariadb-server', 'php', 'php-mysql'],
    ['systemctl', 'start', 'httpd.service'], ['systemctl', 'enable', 'httpd.service'], ['systemctl', 'start', 'mariadb'],
    ['systemctl', 'enable', 'mariadb.service'], ['systemctl', 'restart', 'httpd.service']

    for x in commands_to_run:
        print(subprocess.check_output(x))


loop=True
while loop:
    print_menu()
    choice = input("Enter your choice [1-3]: ")

    if choice=='1':
        print("Deploy LAMP server, selected")
        #Functions go here
        deploy_httpd()
    elif choice=='2':
        print("Do something else")
        #Functions go here
elif choice=='3':
        loop=False
    else:
input("Wrong option selected. Enter any key to try again..")
