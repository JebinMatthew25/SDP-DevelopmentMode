import zipfile
import os

##############################################################################
where_1 = "webapps/ROOT/WEB-INF/web.xml"
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
where_2 = "conf/web.xml"
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
where_3 = "bin/run.bat"
what_3 = '''
rem ################# For DB support ################
'''
with_what_3 = '''
rem ################# For Development Mode ################

set JAVA_OPTS = %JAVA_OPTS% -Dorg.apache.jasper.compiler.Parser.STRICT_QUOTE_ESCAPING=false -Dorg.apache.jasper.compiler.Parser.STRICT_WHITESPACE=false

rem ################# For DB support ################
'''

##############################################################################
where_4 = "webapps/ROOT/WEB-INF/web.xml"
what_4 = '''
                <param-name>development.mode</param-name>
              <param-value>false</param-value>
'''
with_what_4 = '''
                <param-name>development.mode</param-name>
              <param-value>true</param-value>
'''
#############################################################################

def extract_it():
    print("extracting developmode.zip...")
    with zipfile.ZipFile("developmode.zip", 'r') as zip_ref:
        zip_ref.extractall("webapps/ROOT")
        print("done extracting")
    zip_ref.close()

def alter_file(path, what, with_what):
    with open(path, "r") as file:
        content = file.read()
    content = content.replace(what, with_what)
    with open(path, "w") as file:
        content = file.write(content)
    print("Altered " + path)    

if __name__ == "__main__":
    alter_file(where_1, what_1, with_what_1)
    alter_file(where_2, what_2, with_what_2)
    alter_file(where_3, what_3, with_what_3)
    alter_file(where_4, what_4, with_what_4)
    extract_it()
    print("Thank you!")
    print("Credits: Jebin-8730")
