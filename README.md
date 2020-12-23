# KML_To_GMT
This tool parses and extracts geographical and utm coordinates from KML point file (Google Earth) into ASCCI file (PSXY and PSTEXT, wich have GMT templates formats) and Excel sheet with poin names and coordinates. Point names without grammatical accents (utf issues).

Steps to launch the tool:
Set up in command line the path folder where you have the KML files.

Files requiered (respectively):
1. 00_COORDENADAS.py
2. POINTS_GEO.kml (in geographical coordinates)
3. POINTS_UTM.kml (in UTM coordinates)
4. OUTPUT FILE NAME (without any extension) dont recognize accents.

To get 3. or 4. you just need to go to Google Earth and switch from one coodinates to the other one.

Go to the menu "Tools", select "Options"  

![GE-1](https://user-images.githubusercontent.com/52880203/101363317-8c51e700-38a1-11eb-9d49-6372e88adba0.png)

In the pop up window check on Universal Transverse Mercator (UTEM )if you are in Geographical coordinates and you want to get UTM coordinates

![GE-2](https://user-images.githubusercontent.com/52880203/101364371-c7084f00-38a2-11eb-835c-8365ef7ab69c.png)

Go to "Places", select the point, right click, properties and check if the unit system has been changed in the coordinates

![GE-3](https://user-images.githubusercontent.com/52880203/101363548-d33fdc80-38a1-11eb-8fd2-95780593bbdd.png)


To launch the tool, write down in the command line:

![2020-12-07 13_36_41-Window](https://user-images.githubusercontent.com/52880203/101357547-df27a080-3899-11eb-83ae-dcd953f810ca.png)

The output files are: 
- output.pstext (Command used in GMT mapping tool to text maps)

![excel_sheet](https://user-images.githubusercontent.com/52880203/101357293-8821cb80-3899-11eb-95f7-9f3e11999ccb.png)

- output.xlsx (Excel sheet for a report)

![pstext](https://user-images.githubusercontent.com/52880203/101357820-42193780-389a-11eb-870d-53d227c68fb2.png)

Enjoy it :-D

