import sys

from util import *

##############################################################################
where_1 = path_join("webapps", "ROOT", "WEB-INF", "web.xml")
what_1 = "</web-app>"
with_what_1 = '''

    <!-- DEBUG-MODE -->

    <servlet>
        <servlet-name>default</servlet-name>
        <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
        <init-param>
            <param-name>debug</param-name>
            <param-value>0</param-value>
        </init-param>
        <init-param>
            <param-name>mappedfile</param-name>
            <param-value>false</param-value>
        </init-param>
        <init-param>
            <param-name>listings</param-name>
            <param-value>false</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet>
        <servlet-name>jsp</servlet-name>
        <servlet-class>org.apache.jasper.servlet.JspServlet</servlet-class>
        <init-param>
            <param-name>mappedfile</param-name>
            <param-value>false</param-value>
        </init-param>
    </servlet>
</web-app>
'''
#############################################################################
where_2 = path_join("conf", "web.xml")
what_2 = '''
        <init-param>
            <param-name>development</param-name>
            <param-value>false</param-value>
        </init-param>
        <init-param>
            <param-name>reloading</param-name>
            <param-value>false</param-value>
        </init-param>
'''
with_what_2 = '''
        <init-param>
            <param-name>development</param-name>
            <param-value>true</param-value>
        </init-param>
        <init-param>
            <param-name>reloading</param-name>
            <param-value>true</param-value>
        </init-param>
'''
#############################################################################
where_3 = path_join("bin", "run.bat")
what_3 = '''
rem ################# For DB support ################
'''
with_what_3 = '''
rem ################# For Development Mode ################

set JAVA_OPTS = %JAVA_OPTS% -Dorg.apache.jasper.compiler.Parser.STRICT_QUOTE_ESCAPING=false -Dorg.apache.jasper.compiler.Parser.STRICT_WHITESPACE=false

rem ################# For DB support ################
'''

##############################################################################
where_4 = path_join("webapps", "ROOT", "WEB-INF", "web.xml")
what_4 = '''
                <param-name>development.mode</param-name>
              <param-value>false</param-value>
'''
with_what_4 = '''
                <param-name>development.mode</param-name>
              <param-value>true</param-value>
'''


#############################################################################


class DevMode:

    def __init__(self, build_dir, build_name, is_sdp=True):
        self.server_home = get_server_home(build_dir, build_name, is_sdp)

    def dl_extract_dev(self, url):
        dl_extract(url, "developmode.zip", path_join(self.server_home, "webapps", "ROOT"))

    def do_dev_mode(self):
        alter(path_join(self.server_home, where_1), what_1, with_what_1)
        alter(path_join(self.server_home, where_2), what_2, with_what_2)
        alter(path_join(self.server_home, where_3), what_3, with_what_3)
        alter(path_join(self.server_home, where_4), what_4, with_what_4)


if __name__ == '__main__':
    usage = '''

    developmode.zip will be downloaded from the URL and will be applied for sdp build "my_build" in "D:/Build" directory:
        python devmode.py sdp "D:/Build" "my_build" http://build/me/assetexplorer/webhost/ASSETEXPLORER_PRTL_TXLN2_BRANCH_REVIEWED/Apr_13_2020/
    '''

    my_product = sys.argv[1]
    my_build_dir = sys.argv[2]
    my_build = sys.argv[3]

    argv_len = len(sys.argv)
    if argv_len == 4:
        DevMode(my_build_dir, my_build, my_product == "sdp")
    else:
        print(usage)
    input("Press Enter to quit...")
