
from netmiko import ConnectHandler
from datetime import date
import getpass
today = date.today()
conf_time = today.strftime("%m.%d.%Y")


def main():
    # Determine if user wants individual IP or list from file
    ip = input('Enter IP to obtain config or enter "List" to obtain all configs from list in myswitches:')

    # Obtain user and password information from user
    username = input('Enter Device Username: ')
    password = getpass.getpass('Enter Device Password: ')

    # Functions for multiple devices from list or single/new device
    def list_of_devices():
        # Get list of ip_addr from file
        for ip_addr in f:
            ip_addr = ip_addr.strip()

            # Connect to Device
            dev_connect = ConnectHandler(device_type='cisco_ios', ip=ip_addr, username=username, password=password)
            print('Getting running config from switch at ' + ip_addr)

            # Open file to store config
            save_config = open('Config ' + ip_addr + ' ' + conf_time, 'w')
            running_config = dev_connect.send_command('skip-page-display')
            running_config = dev_connect.send_command('show running-config')

            # Print config to screen (toggle off if desired)
            print(running_config)

            # Save above config to file
            save_config.write(running_config)
            save_config.close()

    def single_device():
        # Connect to Device
        dev_connect = ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
        print('Getting running config from switch at ' + ip)

        # Open file to store config
        save_config = open('Config ' + ip + ' ' + conf_time, 'w')
        running_config = dev_connect.send_command('skip-page-display')
        running_config = dev_connect.send_command('show running-config')

        # Print config to screen (toggle off if desired)
        print(running_config)

        # Save above config to file
        save_config.write(running_config)
        save_config.close()

    # Run function to connect to multiple devices or single based on choice
    if ip == 'List' or ip == 'list':
        f = open('myswitches')
        list_of_devices()
    else:
        single_device()


if __name__ == '__main__':
    main()
