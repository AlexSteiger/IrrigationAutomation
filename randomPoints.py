"""
Model exported as python.
Name : Modell
Group : 
With QGIS : 32603
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Modell(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSink('Randompoints', 'randomPoints', type=QgsProcessing.TypeVectorPoint, createByDefault=True, defaultValue='N:/Daten_GG/projekte/2021_EU_BMBF_AddFerti_64130208/Data/Irrigation Automation/Skript/randomPoints.geojson'))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Zufällige Punkte in Grenzen
        alg_params = {
            'EXTENT': '617722.757800000,618015.766100000,4443637.554400000,4444187.645900000 [EPSG:32635]',
            'MAX_ATTEMPTS': 200,
            'MIN_DISTANCE': 1,
            'POINTS_NUMBER': 37,
            'TARGET_CRS': 'ProjectCrs',
            'OUTPUT': parameters['Randompoints']
        }
        outputs['ZuflligePunkteInGrenzen'] = processing.run('native:randompointsinextent', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Randompoints'] = outputs['ZuflligePunkteInGrenzen']['OUTPUT']
        return results

    def name(self):
        return 'Modell'

    def displayName(self):
        return 'Modell'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Modell()
