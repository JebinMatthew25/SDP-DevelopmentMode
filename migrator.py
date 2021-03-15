from util import *
import re


class Migrator:
    migration_sequence = (9300, 9336, 9400, 10000, 10500, 10513, 11000)
    ppm_folder_mapping = {10500: 10.5, 10000: '10000_5'}

    @staticmethod
    def get_next_ppm_num(curr_build_num):
        for stop_build in Migrator.migration_sequence:
            if curr_build_num < stop_build:
                return stop_build

    @staticmethod
    def get_ppm_link(build_num, target_os="windows"):
        build_num = Migrator.ppm_folder_mapping[build_num] if build_num in Migrator.ppm_folder_mapping else build_num
        url = "https://archives.manageengine.com/service-desk/%s/" % build_num
        print(url)

        ppm_name = ""
        with urllib.request.urlopen(url) as html:
            for line in html.read().decode("utf-8").split():
                if ".ppm" in line:
                    ppm_name = line
                    if target_os in ppm_name.lower():
                        break
        print(ppm_name)
        ppm_name = re.findall('"([^"]*)"', ppm_name)[0]
        return url + ppm_name
