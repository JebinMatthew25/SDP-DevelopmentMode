from util import *
import sys


class PortChanger:
    def __init__(self, build_dir, build_name, is_sdp=True):
        self.is_sdp = is_sdp
        self.server_home = get_server_home(build_dir, build_name, is_sdp)

    def change_ports(self, server_port, scheme, db_port):
        change_server_port(self.server_home, server_port, scheme)
        change_db_port(self.server_home, db_port, self.is_sdp)

    def change_ports_simple(self, port_suffix, scheme="http"):
        server_port = port_suffix + "" + port_suffix
        db_port = "654" + port_suffix
        self.change_ports(server_port, scheme, db_port)


if __name__ == '__main__':
    usage = '''
    PortChanger has two modes: Simple and Normal

    Simple:
        The following command sets port as 7676 (https) and db port as 65476 for an sdp running in D:/Build/my_build
        python portChanger.py sdp "D:/Build" "my_build" 76 https
    Normal:
        The following command sets port as 8123 (http) and db port as 65789 for an sdp running in D:/Build/my_build
        python portChanger.py sdp "D:/Build" "my_build" 8123 http 65789 
    '''

    argv_len = len(sys.argv)
    if argv_len > 4:
        my_product = sys.argv[1]
        my_build_dir = sys.argv[2]
        my_build_name = sys.argv[3]
        my_server_port = sys.argv[4]
        my_scheme = sys.argv[5] if argv_len > 5 else "https"
        if argv_len == 7:
            my_db_port = sys.argv[6]
            PortChanger(my_build_dir, my_build_name, "sdp" == my_product).change_ports(my_server_port, my_scheme, my_db_port)
        else:
            PortChanger(my_build_dir, my_build_name, "sdp" == my_product).change_ports_simple(my_server_port, my_scheme)
        print(credit)
    else:
        print(usage)
    input("Press Enter to quit...")
