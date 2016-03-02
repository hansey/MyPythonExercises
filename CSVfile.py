import csv
import time
import os
try:
    from xml.etree import ElementTree as ET
except ImportError:
    from xml.etree import cElementTree as ET
var_limit = 0
var_data_list = []
var_header_list = []
var_addition_create_list = []
var_addition_add_list = []
var_data_path = ""

def header_create(
        var_xml_path, var_data_path_in, var_fai_number,
        bool_is_addition_create, bool_is_addition_add):
    global var_header_list
    global var_data_path
    set_fai_number(var_fai_number)
    if os.path.isfile(var_xml_path):
        var_element_tree = ET.ElementTree()
        var_element_tree.parse(var_xml_path)
        var_element = var_element_tree.getroot()
        var_element_all = var_element.findall('header')
        for var_element_header in var_element_all:
            for var_element_fai in var_element_header:
                var_header_list.append(str(var_element_fai.text))
        var_data_path_in = get_current_data() + "_" + var_data_path_in
        csv_write_file = file(var_data_path_in,'wb')
        csv_writer = csv.writer(csv_write_file,dialect='excel')
        csv_writer.writerow(var_header_list)
        var_header_list = []
        csv_write_file.close()
        var_data_path = var_data_path_in
        if bool_is_addition_create:
            addition_create(var_xml_path)
        if bool_is_addition_add:
            addition_add(var_xml_path)
    else:
        return False

def addition_create(
        var_xml_path):
    global var_addition_create_list
    global var_data_path
    var_data_path_in = var_data_path
    if os.path.isfile(var_xml_path):
        var_element_tree = ET.ElementTree()
        var_element_tree.parse(var_xml_path)
        var_element = var_element_tree.getroot()
        var_element_all = var_element.findall('add1')
        for var_element_add1 in var_element_all:
            for var_element_add in var_element_add1:
                var_addition_create_list.append(str(var_element_add.text))
        csv_write_file = file(var_data_path_in,'ab')
        csv_writer = csv.writer(csv_write_file,dialect='excel')
        csv_writer.writerow(var_addition_create_list)
        csv_write_file.close()

def addition_add(
        var_xml_path):
    global var_addition_add_list
    global var_data_path
    var_data_path_in = var_data_path
    if os.path.isfile(var_xml_path):
        var_element_tree = ET.ElementTree()
        var_element_tree.parse(var_xml_path)
        var_element = var_element_tree.getroot()
        var_element_all = var_element.findall('add2')
        for var_element_add2 in var_element_all:
            for var_element_add in var_element_add2:
                var_addition_add_list.append(str(var_element_add.text))
        csv_write_file = file(var_data_path_in,'ab')
        csv_writer = csv.writer(csv_write_file,dialect='excel')
        csv_writer.writerow(var_addition_add_list)
        csv_write_file.close()

def set_fai_number(
        var_number):
    global var_limit
    var_limit = var_number

def data_receive(
        var_data_in):
    global var_limit
    global var_data_list
    if len(var_data_list) < var_limit:
        var_data_list.append(var_data_in)
    elif len(var_data_list) == var_limit:
        var_data_list.append(var_data_in + next_line())
        return var_data_list
    else:
        return 0

def data_writer():
    global var_data_list
    global var_data_path
    var_data_path_in = var_data_path
    csv_write_file = file(var_data_path_in,'ab')
    csv_writer = csv.writer(csv_write_file,dialect='excel')
    csv_writer.writerow(var_data_list)
    var_data_list = []
    csv_write_file.close()

def get_current_data():
    return time.strftime("%Y_%m_%d",time.localtime(time.time()))

def get_current_time():
    return time.strftime("%Y_%m_%d",time.localtime(time.time()))

def next_line():
    return os.linesep

header_create("test.xml","3.csv",3,True,True)
data_receive("1")
data_receive("2")
data_receive("3")
data_writer()