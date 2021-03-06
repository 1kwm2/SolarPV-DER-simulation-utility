# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:20:55 2020

@author: splathottam
"""

import six
from pvder.grid_components import Grid,BaseValues

steadystate_solver_spec = {'SLSQP':{'ftol': 1e-10, 'disp': True, 'maxiter':10000},
               'nelder-mead':{'xtol': 1e-8, 'disp': True, 'maxiter':10000}}

if six.PY3:
    string_type = (str)
elif six.PY2:
    string_type = (str,unicode)
           
DER_argument_spec = {'derId':{'default_value':None,'type':string_type},
                         'powerRating':{'default_value':None,'type':(int,float)},
                         'VrmsRating':{'default_value':None,'type':(int,float)},'Vdcrated':{'default_value':None,'type':(int,float)},
                         'gridModel':{'default_value':None,'type':Grid},
                         'verbosity':{'default_value':'INFO','type':string_type},'identifier':{'default_value':'','type':string_type},
                         'derConfig':{'default_value':{},'type':dict},
                         'gridVoltagePhaseA':{'default_value':None,'type':complex},
                         'gridVoltagePhaseB':{'default_value':None,'type':complex},
                         'gridVoltagePhaseC':{'default_value':None,'type':complex},
                             'gridFrequency':{'default_value':None,'type':(int,float)},
                             'standAlone':{'default_value':True,'type':bool},'steadyStateInitialization':{'default_value':True,'type':bool},
                             'allowUnbalancedM':{'default_value':False,'type':bool},
                             'ia0':{'default_value':None,'type':complex},'xa0':{'default_value':None,'type':complex},
                             'ua0':{'default_value':None,'type':complex},
                             'xDC0':{'default_value':None,'type':float},
                             'xP0':{'default_value':None,'type':float},'xQ0':{'default_value':None,'type':float}}