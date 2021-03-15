from devmode import DevMode
from util import *
import sys


class Installer:
    def __init__(self, build_dir, build_name, is_sdp=True):
        self.is_sdp = is_sdp
        self.build_name = build_name
        self.base_dir = path_join(build_dir, self.build_name)
        self.server_home = get_server_home(build_dir, self.build_name, self.is_sdp)
        logging.info("ServerHome: %s", self.server_home)

    def dl_extract(self, url):
        if self.is_sdp:
            try:
                dl_extract(url, "AdventNet_ManageEngine_ServiceDesk_windows_64bit_unpack.zip", self.base_dir)
            except Exception as e:
                logging.info("Trying a different file")
                dl_extract(url, "AdventNet_ManageEngine_ServiceDesk_windows_64bit.zip", self.base_dir)
        else:
            try:
                dl_extract(url, "AdventNet_ManageEngine_AssetExplorer_windows_64bit_unpack.zip", self.base_dir)
            except Exception as e:
                logging.info("Trying a different file")
                dl_extract(url, "AdventNet_ManageEngine_AssetExplorer_windows_64bit.zip", self.base_dir)

    @time_log
    def milestone(self, build_num, dev=False, run=True):
        if self.is_sdp:
            if 11001 >= int(build_num) >= 11007:
                url = 'http://build/me/servicedeskplus/milestones/SERVICEDESKPLUS_ISSUES_BRANCH_REVIEWED/SERVICEDESKPLUS_%s/' % build_num
            else:
                url = 'http://build/me/servicedeskplus/milestones/SERVICEDESKPLUS_REVIEWED/SERVICEDESKPLUS_%s/' % build_num
        else:
            url = 'http://build/me/assetexplorer/milestones/ASSETEXPLORER_REVIEWED/ASSETEXPLORER_%s/' % build_num
        self.webhost(url, dev, run)

    @time_log
    def webhost(self, url, dev=False, run=True):
        self.dl_extract(url)
        if dev:
            developer = DevMode(self.base_dir, self.build_name, self.is_sdp)
            developer.dl_extract_dev(url)
            developer.do_dev_mode()
        if run:
            run_app(self.server_home)


if __name__ == '__main__':
    usage = '''
    Milestone: 
        python installer.py sdp "D:/Build" m my_build 11000 
    WebHost: 
        python installer.py ae "D:/Build" wh my_build http://build/me/assetexplorer/webhost/ASSETEXPLORER_PRTL_TXLN2_BRANCH_REVIEWED/Apr_13_2020/
    '''
    print(sys.argv)
    if len(sys.argv) > 5:
        my_product = sys.argv[1]
        my_build_dir = sys.argv[2]
        my_build = sys.argv[4]
        my_arg = sys.argv[5]
        if sys.argv[3] == 'm':
            Installer(my_build_dir, my_build, "sdp" == my_product).milestone(my_arg)
            print(credit)
        if sys.argv[3] == 'wh':
            Installer(my_build_dir, my_build, "sdp" == my_product).webhost(my_arg)
            print(credit)
        else:
            print(usage)
    else:
        print(usage)
    input("Press Enter to quit...")
