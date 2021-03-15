from functools import wraps
from os.path import join as path_join

import os
import urllib.request
import tempfile
import zipfile
import logging
import subprocess
import time

logging.basicConfig(format='%(message)s', level=logging.INFO)


def time_log(func):
    @wraps(func)
    def get_time_log(*args, **kwargs):
        t = time.time()
        ret = func(*args, **kwargs)
        logging.info("%s took %.2f seconds" % (func.__name__, time.time() - t))
        return ret

    return get_time_log


@time_log
def download(url, file_name):
    logging.info("Downloading %s...", file_name)
    web_file = urllib.request.urlopen(url + file_name)
    out_file = tempfile.TemporaryFile()
    out_file.write(web_file.read())
    logging.info("Downloaded %s", file_name)
    return out_file


@time_log
def extract(file, path):
    logging.info("Extracting %s", file.name)
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(path)
    file.close()
    logging.info("Extracted to %s", path)


def alter(file_path, what, with_what):
    with open(file_path, 'w+') as f:
        s = f.read()
        s = s.replace(what, with_what)
        f.write(s)


def dl_extract(url, file_name, path):
    url = url if url.endswith("/") else url + "/"
    dl_file = download(url, file_name)
    extract(dl_file, path)


def get_server_home(build_dir, build_name, is_sdp=True):
    return path_join(build_dir, build_name, "AdventNet", "ME", "ServiceDesk" if is_sdp else "AssetExplorer")


def wrap_cmd_ext(server_home, cmd_name):
    return path_join(server_home, "bin", cmd_name + ".bat" if os.name == 'nt' else ".sh")


def run_app(server_home):
    cmd = wrap_cmd_ext(server_home, "run")
    logging.info("Running %s", cmd)
    subprocess.Popen([cmd], cwd=path_join(server_home, "bin"), shell=True).communicate()


def change_server_port(server_home, port, scheme="https"):
    cmd = wrap_cmd_ext(server_home, "changeWebServerPort")
    subprocess.Popen([cmd, str(port), scheme], cwd=path_join(server_home, "bin"), shell=True, stdin=subprocess.PIPE).communicate(input=b'y')


def change_db_port(server_home, port, is_sdp):
    cmd = wrap_cmd_ext(server_home, "changeDBServer")
    p = subprocess.Popen([cmd, '--console'], cwd=path_join(server_home, "bin"), shell=True, stdin=subprocess.PIPE)
    if is_sdp:
        p.communicate(input=b'1\nlocalhost\n' + str(port).encode() + b'\nsdpadmin\nsdp@123\nservicedesk')
    else:
        p.communicate(input=b'1\nlocalhost\n' + str(port).encode() + b'\nsdpadmin\nsdp@123\nassetexplorer')


# Contributors shall add their names here
credit = '''
                    jebin-8730
'''
