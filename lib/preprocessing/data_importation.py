'''
Note: Re-save arrays in the correct format directly for easy loading
'''

import os
import numpy as np
import warnings

class DataImporter():
    def __init__(self, path):
        self.path = path
    
    def load_npy_data(self):
        '''
        Loads three separate NPY files in specified path folder:
            - data.npy: format (rx,ry,s0,s1) uint8
            - eulers.npy: format (rx,ry,3) float
            - labels.npy: format (rx,ry)
        '''
        ### LOADING DRM DATA
        data = self._open_file('data.npy')
        rx, ry, s0, s1 = data.shape
        data = data.reshape((rx*ry,s0*s1))

        ### LOADING EULER ANGLES
        eulers = self._open_file('eulers.npy')
        eulers = eulers.reshape((rx*ry,3))
        
        ### LOADING REFERENCE SEGMENTATION
        labels = self._open_file('labels.npy')
        labels = labels.ravel()
        
        ### RETURNING A DATASET DICTIONARY
        dataset = {
            'data':data, 
            'eulers':eulers,
            'labels':labels,
            'spatial_resol':(rx,ry), 
            'angular_resol':(s0,s1),
            }

        return dataset
        
    def _open_file(self, fname):
        '''Attempts to open specified .npy file'''
        file = os.path.join(self.path, fname)
        if os.path.isfile(file):
            data = np.load(file)
            return data
        else:
            warnings.warn(f'File: {fname} could not be loaded.')
        