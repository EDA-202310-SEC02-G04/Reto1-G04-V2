"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""


# Construccion de modelos


def new_data_structs(data_organization):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=data_organization,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["data"], data)

    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["data"])

def com_req_1(data_1, data_2):
    return (float(data_1['Total saldo a pagar']) < float(data_2['Total saldo a pagar']))

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    datos_ordenados = merg.sort(data_structs, com_req_1)
    iterado = lt.iterator(datos_ordenados)
    lista_aux = {
        "data": None
    }
    lista_aux["data"] = lt.newList(datastructure="ARRAY_LIST")
    for dic in iterado:
        if dic['Año'] not in lista_aux:
            lt.addLast(lista_aux, dic)
    return lista_aux
     

def com_req_2(data_1, data_2):
    return (float(data_1['Total saldo a favor']) > float(data_2['Total saldo a favor']))

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    datos_ordenados = merg.sort(data_structs, com_req_2)
    iterado = lt.iterator(datos_ordenados)
    lista_aux = {
        "data": None
    }
    lista_aux["data"] = lt.newList(datastructure='ARRAY_LIST')
    for dic in iterado:
        if dic['Año'] not in lista_aux:
            lt.addLast(lista_aux, dic)
    return lista_aux

def com_req_3(data_1, data_2):
    return (float(data_1['Total retenciones']) > float(data_2['Total retenciones']))

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    datos_ordenados = merg.sort(data_structs, com_req_3)
    iterado = lt.iterator(datos_ordenados)
    lista_aux = {
        "data": None
    }
    lista_aux["data"] = lt.newList(datastructure="ARRAY_LIST")
    for dic in iterado:
        if dic["Año"] not in lista_aux:
            lt.addLast(lista_aux, dic)
    return lista_aux


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lista=data_structs
    lista_grande=ins.sort(lista, sort_criteria_nomina)
    j=data_size(lista_grande)-1
    respuesta=[]
    anioo=2012
    anio=(lista_grande)[j]['Año']
    dato=tuple(((lista_grande)[j]['Nombre subsector económico']),anio)
    while j>-1:
        if anio==anioo:
            lt.addLast(respuesta, dato)
            anioo+=1
            j=data_size(lista_grande)-1
        else:
            j+=1
    return respuesta
        
    
    

def comparacion_año(data_1, data_2):
    return (data_1["Año"] < data_2["Año"])

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    """
    lista = {
        "data": None
    }
    lista["data"] = lt.newList(datastructure = data_structs, cmpfunction=comparacion_año)
    """
    data_structs = lt.newList("ARRAY_LIST")
    lista = data_structs

    años = set([elemento[0] for elemento in lista])
    resultados_descuentos = []

    for año in años:
        actividades_año = [elemento for elemento in lista if elemento[0] == año]  
        subsectores = set([(elemento[3], elemento[4], elemento[5], elemento[6]) for elemento in actividades_año])
        descuentos_por_subsector = []

        for codigo_sector, sector, codigo_subsector, subsector in subsectores:
            descuento_total_subsector = sum([elemento[45] for elemento in actividades_año if elemento[3] == codigo_sector and elemento[4] == sector and elemento[5] == codigo_subsector and elemento[6] == subsector])
            descuentos_por_subsector.append([codigo_sector, sector, codigo_subsector, subsector, descuento_total_subsector])

        max_descuento_subsector = max(descuentos_por_subsector, key=lambda x: x[4])
        resultados_descuentos.append([año, max_descuento_subsector[0], max_descuento_subsector[1], max_descuento_subsector[2], max_descuento_subsector[3]])
    
    resultados = []

    for año, codigo_sector, sector, codigo_subsector, subsector in resultados_descuentos:
        actividades_año_subsector = ([elemento for elemento in lista if elemento[3] == codigo_sector and elemento[4] == sector and elemento[5] == codigo_subsector and elemento[6] == subsector])

        total_ingresos = sum([elemento[25] for elemento in actividades_año_subsector])
        total_costosygastos = sum([elemento[31] for elemento in actividades_año_subsector])
        total_saldo_pagar = sum([elemento[57] for elemento in actividades_año_subsector])
        total_saldo_favor = sum([elemento[58] for elemento in actividades_año_subsector])
        

        resultados.append(año, codigo_sector, sector, codigo_subsector, total_ingresos, total_costosygastos, total_saldo_pagar, total_saldo_favor)


    subsector_max_descuento = max_descuento_subsector[2]
    actividades_subsector = [elemento for elemento in actividades_año if elemento[5] == subsector_max_descuento]
    actividades_unicas = set([(elemento[1], elemento[2]) for elemento in actividades_subsector])
    descuentos_por_actividad = []
    resultados_actividades = []

    for codigo_actividad, actividad in actividades_unicas:
        descuento_total_actividad = sum(elemento[45] for elemento in actividades_subsector if elemento[1] == codigo_actividad and elemento[2] == actividad)
        descuentos_por_actividad.append([codigo_actividad, actividad, subsector_max_descuento, descuento_total_actividad])

    descuentos_por_actividad_ordenados = quk.sort(descuentos_por_actividad, key=lambda x: x[3], reverse=True)
    actividades_mas_aportaron = descuentos_por_actividad_ordenados[:3]
    actividades_menos_aportaron = descuentos_por_actividad_ordenados[-3:]

    resultados_actividades.append([año, subsector_max_descuento, actividades_mas_aportaron, actividades_menos_aportaron])

    return resultados, resultados_actividades


def req_6(data_structs, anio_pedido):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    lista_por_anio=ins.sort(data_structs, sort_criteria)
    lista_agrupada_anio=[[],[],[],[],[],[],[],[],[],[]]
    anioo=2012
    indice_anioo=0
    indice_grande=0
    lista_sectores=[[],[],[],[],[],[],[],[],[],[]]
    while lt.size(lista_por_anio)>0:
        while lista_por_anio[indice_grande]['Año']==anioo:
            lt.addLast(lista_agrupada_anio[indice_anioo], lista_por_anio[indice_grande])
            lt.deleteElement(lista_por_anio, indice_grande)
            indice_grande+=1
        indice_anioo+=1
        indice_grande=0
    indice_anioo=0
    while indice_anioo<lt.size(lista_agrupada_anio):
        sa.sort((lista_agrupada_anio[indice_anioo]), sort_criteria_sec_economico)
        indice_anioo+=1
    indice_anioo=0
    inicio=0
    indice=inicio
    while indice_anioo<lt.size(lista_agrupada_anio):
        while indice<lt.size(lista_agrupada_anio[indice_anioo]):
            if lista_agrupada_anio[indice_anioo][indice]['Nombre sector económico']==lista_agrupada_anio[indice_anioo][inicio]['Nombre sector económico']:
                indice+=1
            else:
                sectoranio=lt.lastElement(sa.sort((lt.subList(lista_agrupada_anio[indice_anioo], inicio, (indice+1-inicio))), sort_criteria_ingresos_netos))
                
            lt.addFirst((lista_sectores[0]),tuple((lista_agrupada_anio[indice_anioo][inicio]['Actividad económica']),sectoranio))
            inicio=indice+1
            indice=inicio 
        indice_anioo+=1
    respuesta=lista_sectores[(anio_pedido-2012)]
    return respuesta

def req_7(data_structs, año_inicio, año_fin, N_valor):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    data_structs = lt.newList("ARRAY_LIST")

    datos_ordenados = quk.sort(data_structs, key=lambda x: x[31])
    datos_rango = [x for x in datos_ordenados if x[0] >= año_inicio and x[0] <= año_fin]

    top = req_7(datos_rango, N_valor)

    return top


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    return data_1["Año"] > data_2["Año"]

def sort_criteria_nomina(data_1, data_2):
    return data_1["Costos y gastos nómina"] > data_2["Costos y gastos nómina"]

def sort_criteria_sec_economico(data_1, data_2):
    return data_1["Nombre sector económico"] > data_2["Nombre sector económico"]

def sort_criteria_ingresos_netos(data_1, data_2):
    return data_1["Total ingresos netos"] > data_2["Total ingresos netos"]

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    lista=sa.sort(data_structs["data"], sort_criteria)
    return lista
    pass
