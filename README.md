# KML_To_GMT
This tool parse and extract points coordinates from KML file (Google Earth) to ASCCI file with PSXY and PSTEXT GMT templates

Steps to lunch it:
Set up in command line the path folder where you have the KML files.

Files requiered (respectively):
1. 00_COORDENADAS.py
2. TUNELS_GEO.kml
3. TUNELS_UTM.kml
4. output (name of the outputfil)
Enjoy it!

Write down the followers files
![2020-12-07 13_36_41-Window](https://user-images.githubusercontent.com/52880203/101352571-a59f6700-3892-11eb-927e-257c7c8419ff.png)

The output files are: 
- output.pstext (Command used in GMT mapping tool to text maps)

![pstext](https://user-images.githubusercontent.com/52880203/101352822-fd3dd280-3892-11eb-9a62-53d470d6a831.png)

- output.xlsx (Excel sheet for a report)

![excel_sheet](https://user-images.githubusercontent.com/52880203/101352662-cb2c7080-3892-11eb-8688-f194c9efc1f0.png)

