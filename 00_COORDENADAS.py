#!python2.7
import sys
from xml.dom.minidom import parse
import xml.dom.minidom
import xlsxwriter
import win32com.client as win32
import os


# this are the arguments passed to the script
# argv[0] is the name of the script
# argv[1] is the name kml file in geo unit
# argv[2] is the name kml file in utm unit
# argv[3] is the output file without extension

# open input file
#input_file = open(sys.argv[1], "r")
points = []

#open output file
#output_file = open(sys.argv[2], "w")
class Point:
	coord_geo_x = 0.0
	coord_geo_y = 0.0
	coord_geo_z = 0.0
	coord_utm_x = 0.0
	coord_utm_y = 0.0
	coord_utm_z = 0.0
	name = "unknown"

	def debugPrint(self):
		print self.point.name
		print self.point.coord_geo_x, self.point.coord_geo_y, self.point.coord_geo_z 
		print self.point.coord_utm_x, self.point.coord_utm_y, self.point.coord_utm_z
 
DOMTree = xml.dom.minidom.parse(sys.argv[1])
collection = DOMTree.documentElement
Placemarks = collection.getElementsByTagName("Placemark")
for Placemark in Placemarks:
	point = Point()
	xmlname = Placemark.getElementsByTagName('name')[0]
	point.name = xmlname.childNodes[0].data
	xmlpoint = Placemark.getElementsByTagName('Point')[0]
	xmlcoord = Placemark.getElementsByTagName('coordinates')[0]
	coords = xmlcoord.childNodes[0].data.split(",")
	point.coord_geo_x = float(coords[0])
	point.coord_geo_y = float(coords[1])
	point.coord_geo_z = float(coords[2])
	points.append(point)

DOMTree = xml.dom.minidom.parse(sys.argv[2])
collection = DOMTree.documentElement
Placemarks = collection.getElementsByTagName("Placemark")
for Placemark in Placemarks:
	point = Point()
	xmlname = Placemark.getElementsByTagName('name')[0]
	name = xmlname.childNodes[0].data
	point = None
	for p in points:
		if (p.name == name):
			point = p
			break
	xmlpoint = Placemark.getElementsByTagName('Point')[0]
	xmlcoord = Placemark.getElementsByTagName('coordinates')[0]
	coords = xmlcoord.childNodes[0].data.split(",")
	point.coord_utm_x = float(coords[0])
	point.coord_utm_y = float(coords[1])
	point.coord_utm_z = float(coords[2])
	points.append(point)

# PSTEXT
output_file = open(sys.argv[3] + ".pstext", "w")
for p in points:
	output_file.write(str(p.coord_geo_x))
	output_file.write(" ")
	output_file.write(str(p.coord_geo_y))
	output_file.write(" ")
	output_file.write("5")
	output_file.write(" ")
	output_file.write("0")
	output_file.write(" ")
	output_file.write("1")
	output_file.write(" ")
	output_file.write("BC")
	output_file.write(" ")
	output_file.write("I")
	output_file.write(" ")
	output_file.write(p.name)
	output_file.write(" ")
	output_file.write("\n")
output_file.close()

# ASCII - 
output_file = open(sys.argv[3] + ".csv", "w")
for p in points:
	output_file.write(str(p.coord_geo_x))
	output_file.write(" ")
	output_file.write(str(p.coord_geo_y))
	output_file.write("\n")
output_file.close()

# excel
workbook = xlsxwriter.Workbook(sys.argv[3] + ".xlsx")

cell_format_table = workbook.add_format({'bold': True, 'font_color': 'white'})
cell_format_table.set_bg_color('#004C99')
cell_format_table.set_text_wrap()
cell_format_table.set_align('center')
cell_format_table.set_align('top')
cell_format_table.set_border(1)
#cell_format_table.set_align(vcenter)
cell_format_table.set_center_across()

cell_format_line = workbook.add_format()
cell_format_line.num_format = '0.0000'
cell_format_line.set_border(1)
cell_format_line.set_center_across()

current_sheet = workbook.add_worksheet("Sheet")

current_sheet.write(0, 0, u"Punto PGA", cell_format_table)
current_sheet.write(0, 1, u"Nombre de Estacion", cell_format_table)
current_sheet.write(0, 2, u"Longitud", cell_format_table)
current_sheet.write(0, 3, u"Latitud", cell_format_table)
current_sheet.write(0, 4, u"ESTE (m)", cell_format_table)
current_sheet.write(0, 5, u"NORTE (m)", cell_format_table)

line = 1
for p in points:
	current_sheet.write(line, 0, "PT0-" + str(line).zfill(2), cell_format_line)
	current_sheet.write(line, 1, p.name, cell_format_line)
	current_sheet.write(line, 2, p.coord_geo_x, cell_format_line)
	current_sheet.write(line, 3, p.coord_geo_y, cell_format_line)
	current_sheet.write(line, 4, p.coord_utm_x, cell_format_line)
	current_sheet.write(line, 5, p.coord_utm_y, cell_format_line)
	line = line + 1
workbook.close()

f = open(sys.argv[3] + ".xlsx", "r")
fullpath = os.path.realpath(f.name)
f.close()
print fullpath
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fullpath)
ws = wb.Worksheets("Sheet")
ws.Columns.AutoFit()
wb.Save()
excel.Application.Quit()

