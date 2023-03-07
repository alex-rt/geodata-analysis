from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd
from src.utils.cords import dms2dd


class Censo00(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2000/microdatos/iter/00_nacional_2000_iter_txt.zip"
    route:str = "data/ITER_NALTXT00.csv"
    
    def __preprocessing__(self):
        self.geodata = gpd.read_file('data/ITER_NALCSV20.csv')#Change
        self.geodata = self.geodata.MUN.str.cat(self.geodata.LOC)
        self.geodata = self.geodata[['NOM_LOC', 'POBTOT', 'geometry', 'CVE_MUN']]

    def __anaylsis__(self):
        self.geodata['LATITUD'] = self.geodata['LATITUD'].apply(dms2dd)
        self.geodata['LONGITUD'] = self.geodata['LONGITUD'].apply(dms2dd)
        self.geodata = gpd.GeoDataFrame(self.geodata, geometry=gpd.points_from_xy(self.geodata.LONGITUD, self.geodata.LATITUD))

        print(self.geodata)
