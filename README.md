# KML_To_GMT
This tool parse and extract geographical and utm coordinates from KML point file (Google Earth) into ASCCI file (PSXY and PSTEXT GMT templates) and excel sheet

Steps to lunch the tool:
Set up in command line the path folder where you have the KML files.

Files requiered (respectively):
1. 00_COORDENADAS.py
2. POINTS_GEO.kml (in geographical coordinates)
3. POINTS_UTM.kml (in UTM coordinates)
4. output (name of the outputfil)

To get 3. or 4. you just need to go to Google Earth and change the parameter

Enjoy it!

To launch the tool, write down in the command line:
![2020-12-07 13_36_41-Window](https://user-images.githubusercontent.com/52880203/101357547-df27a080-3899-11eb-83ae-dcd953f810ca.png)

The output files are: 
- output.pstext (Command used in GMT mapping tool to text maps)

![excel_sheet](https://user-images.githubusercontent.com/52880203/101357293-8821cb80-3899-11eb-95f7-9f3e11999ccb.png)

- output.xlsx (Excel sheet for a report)

![pstext](https://user-images.githubusercontent.com/52880203/101357820-42193780-389a-11eb-870d-53d227c68fb2.png)

