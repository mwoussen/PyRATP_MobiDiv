from openalea.core import *

from PyRATP.pyratp import skyvault
from PyRATP.pyratp import grid
from PyRATP.pyratp import vegetation
from PyRATP.pyratp import micrometeo
from PyRATP.pyratp import runratp
from PyRATP.pyratp import mtg_extract
from PyRATP.pyratp import can2riri
from PyRATP.pyratp.RATP2VTK import RATP2VTK
from PyRATP.pyratp.RATP2VTK import RATPVOXELS2VTK
from PyRATP.pyratp.RATP2VTK import PlantGL2VTK
from PyRATP.pyratp import Nallocate



read_grid = grid.Grid.read
read_vgx = grid.Grid.readVgx
fill_grid = grid.Grid.fill

read_skyvault = skyvault.Skyvault.read
read_vegetation = vegetation.Vegetation.read
read_micrometeo = micrometeo.MicroMeteo.read

DoAll = runratp.runRATP.DoAll
DoIrradiation = runratp.runRATP.DoIrradiation
extract_leaves = mtg_extract.extract_leaves
can2riri = can2riri.can2riri
Nallocate = Nallocate.Nallocate.N_distrib

class ExtractColumn( Node ):
    """ Extract column based on str
    """
    header = ['']
    index = [0]

    def __init__(self):

        Node.__init__(self)

        funs= self.header
        self.add_input( name = "column", interface = IEnumStr(funs), value = funs[0])
        self.add_input( name = "array" )
        self.add_output( name = "array", interface = None)

    def __call__(self, inputs):
        col= inputs[0]
        a = inputs[1]
        print('col ', col)
        try:
            i = self.index[self.header.index(col)]
            self.set_caption(col)
        except Exception as e:
            if col.isdigit():
                i = int(col)
                col = self.header[i]
                self.set_caption(col)
            else:
                raise e
        return a[:,i],

class ExtractTime(ExtractColumn):
    header = """iteration
    day
    hour
    entity
    radiation (w/m2)
    Air Temperature
    Photosynthesis
    Transpiration
    Leaf Surface Area
    """.split('\n')
    header = [x.strip() for x in header]
    index = range(len(header))


