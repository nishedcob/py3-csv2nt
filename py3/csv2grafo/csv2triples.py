#! /usr/bin/env python3
from data_definition import *
from prefixes import PREFIXES
import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Convertir CSV en Tuplas')
    arg_parser.add_argument("--skip-head", type=int, help="saltar un numero de lineas del csv antes de empezar")
    arg_parser.add_argument("--max-lines", type=int, help="numero maximo de lineas que leer")
    arg_parser.add_argument("--in-file", help="archivo entrante (.csv)", required=True)
    arg_parser.add_argument("--out-file", help="archivo saliente (.nt)")
    args = arg_parser.parse_args()

    numero_linea = 0
    archivo_entrada = open(args.in_file, "r")
    archivo_salida = None if args.out_file is None else open(args.out_file, "w")
    numero_lineas_saltar = 0 if args.skip_head is None else args.skip_head
    max_lineas = -1 if args.max_lines is None else args.max_lines
    num_col = len(DATA_COLUMNS)
    subject_nodes = []
    object_nodes = []
    for linea_entrante in archivo_entrada:
        numero_linea += 1
        if numero_lineas_saltar > 0:
            if numero_linea <= numero_lineas_saltar:
                continue
        elif max_lineas > -1:
            if numero_linea >= numero_lineas_saltar + max_lineas:
                break
        columnas_entrantes = linea_entrante.split(",")
        num_col_ent = len(columnas_entrantes)
        nodo_value = DATA_RESOURCE_MAP['value']['value_prefix'] + columnas_entrantes[DATA_ID]
        for key, value in DATA_RESOURCE_MAP['value']['value_proc'].items():
            if key == 'rm':
                for rm in value:
                    nodo_value = nodo_value.replace(rm, "")
        node = "<%s%s>" % (PREFIXES[DATA_RESOURCE_MAP['value']['prefix']], nodo_value)
        subject_nodes.append(node)
        if num_col_ent == num_col:
            for i in range(num_col):
                predicate = "<%s%s>" % (PREFIXES[DATA_COLUMNS[i]['predicate']['prefix']],
                                        DATA_COLUMNS[i]['predicate']['value'])
                value = ""
                if DATA_COLUMNS[i]['type'] == DATA_VALUE:
                    value = '"%s"' % (columnas_entrantes[i])
                    if value == '""':
                        continue
                elif DATA_COLUMNS[i]['type'] == DATA_RESOURCE:
                    value = "<%s%s%s>" % (PREFIXES[DATA_COLUMNS[i]['value']['prefix']],
                                          DATA_COLUMNS[i]['value']['value_prefix'], columnas_entrantes[i].capitalize()
                                          .replace("\n", ""))
                    object_nodes.append(value)
                else:
                    continue
                tuple = "%s %s %s ." % (node, predicate, value)
                if archivo_salida is None:
                    print(tuple)
                else:
                    archivo_salida.write("%s\n" % tuple)
                    archivo_salida.flush()
        else:
            if num_col_ent < num_col:
                for i in range(num_col_ent):
                    predicate = "<%s%s>" % (PREFIXES[DATA_COLUMNS[i]['predicate']['prefix']],
                                            DATA_COLUMNS[i]['predicate']['value'])
                    value = ""
                    if DATA_COLUMNS[i]['type'] == DATA_VALUE:
                        value = '"%s"' % (columnas_entrantes[i])
                    elif DATA_COLUMNS[i]['type'] == DATA_RESOURCE:
                        value = "<%s%s%s>" % (PREFIXES[DATA_COLUMNS[i]['value']['prefix']],
                                              DATA_COLUMNS[i]['value']['value_prefix'], columnas_entrantes[i]
                                              .capitalize().replace("\n", ""))
                    else:
                        continue
                    tuple = "%s %s %s ." % (node, predicate, value)
                    if archivo_salida is None:
                        print(tuple)
                    else:
                        archivo_salida.write("%s\n" % tuple)
                        archivo_salida.flush()
            else:
                for i in range(num_col):
                    predicate = "<%s%s>" % (PREFIXES[DATA_COLUMNS[i]['predicate']['prefix']],
                                            DATA_COLUMNS[i]['predicate']['value'])
                    value = ""
                    if DATA_COLUMNS[i]['type'] == DATA_VALUE:
                        value = '"%s"' % (columnas_entrantes[i])
                    elif DATA_COLUMNS[i]['type'] == DATA_RESOURCE:
                        value = "<%s%s%s>" % (PREFIXES[DATA_COLUMNS[i]['value']['prefix']],
                                              DATA_COLUMNS[i]['value']['value_prefix'], columnas_entrantes[i]
                                              .capitalize().replace("\n", ""))
                    else:
                        continue
                    tuple = "%s %s %s ." % (node, predicate, value)
                    if archivo_salida is None:
                        print(tuple)
                    else:
                        archivo_salida.write("%s\n" % tuple)
                        archivo_salida.flush()
    archivo_entrada.close()
    if archivo_salida is not None:
        archivo_salida.close()
    subject_nodes = set(subject_nodes)
    # print("Subject Nodes:\n", subject_nodes)
    print("Subject Nodes:")
    for subject_node in subject_nodes:
        print(subject_node)
    object_nodes = set(object_nodes)
    # print("Object Nodes:\n", object_nodes)
    print("Object Nodes:")
    for object_node in object_nodes:
        print(object_node)