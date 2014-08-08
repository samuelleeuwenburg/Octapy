# -*- coding: utf-8 -*-

import note
import json

class Scale:
    ''' Build a scale by passing a root note (tonic) and scale name '''

    def __init__(self, tonic, scaleName, degree = 1):
        self.scale = self.calculateScale(tonic, scaleName, degree)

    def getScale(self):
        ''' Returns scale as an array '''
        return self.scale 
            
    def calculateScale(self, tonic, scaleName, degree): 
        # scales/mode available
        f = open('./patterns/scales.json')
        scales = json.loads(f.read())
        f.close()
        
        # order scale pattern by given degree
        index = int(degree) - 1
        head = scales[scaleName][0:index]             
        tail = scales[scaleName][index:len(scales[scaleName])]    
        scaleOrder = tail + head            
        
        # build the scale by starting with the root note
        scale = [tonic]
        for i, step in enumerate(scaleOrder):
            n = note.new(scale[i].name, scale[i].accidental)
            n.transpose(step)
            scale.append(n)

        return scale


def new(tonic, scaleName, degree = 1):
    return Scale(tonic, scaleName, degree)
    
