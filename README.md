###SDP-Tools

----

#### Overview
This project has `.py` files and `.bat` files which can be used to install AE/SDP zips, change app and db ports, download and apply developmode, etc.

### Requirements:
- Python3 Added to path

### Setup Instructions (Windows):
- Download the project in your desired location
- Add the bat_files folder to your PATH
- Open init.bat and set BUILDS_DIR value to the folder where you'll hold all the builds.
- Set PY_DIR to the current location where the python files reside.
- Use corresponding .bat files to perform corresponding actions detailed below.
- All .bat files can be appended with `_ae` for their ae versions.

---

#### 1.1: Zip-Install AE/SDP Milestone
On any cmd, type the following to install SDP 11140 to BUILDS_DIR\my_build and start it up.

`mile my_build 11140`

#### 1.2: Zip-Install AE/SDP Webhost
The following will install SDP 11140 to BUILDS_DIR\sdp11140 and start it up.

`wh my_build <url>`

---

#### 2.1: Change Port (ShortVersion)
The following will set server port to `8080` (https as default) and db port to 654`80` on BUILDS_DIR\my_build.

`chprt my_build 80`

#### 2.2: Change Port (FullVersion)
The following will set server port to `9123` (`http`) and db port to `65789` on BUILDS_DIR\my_build.

`chprt my_build 9123 http 65789`

---

#### 3.1: Open default PG database
Opens postgres db running in port 65432

`db`

#### 3.2: Open PG database (specific port, specific db)
Opens postgres db running in port 65123 and opens a db named sdp_prod

`db -p 65123 -db sdp_prod`

---

Go to product home and paste this file.
Place developmentmode.zip downloaded from your build and place it in product home.
Run this file.
