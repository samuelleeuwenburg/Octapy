# -*- coding: utf-8 -*-

import note
import json
import output

class Scale:
    ''' Build a scale by passing a root note (tonic) and scale name '''

    def __init__(self, tonic, name, degree = 1):
        self.tonic = tonic
        self.name = name
        self.degree = degree

        self.scale = self.calculateScale()


    def getScale(self):
        ''' Returns scale as an array '''
        return self.scale 
            
    def calculateScale(self): 
        # scales/mode available
        f = open('./patterns/scales.json')
        scales = json.loads(f.read())
        f.close()

        try:
            scales[self.name]
        except KeyError, e:
            output.warning('Can\'t find a chord named ' + self.name + ', will default to maj7')
            self.name = 'maj7'
        
        # order scale pattern by given degree
        index = int(self.degree) - 1
        head = scales[self.name][0:index]             
        tail = scales[self.name][index:len(scales[self.name])]    
        scaleOrder = tail + head            
        
        # build the scale by starting with the root note
        scale = [self.tonic]
        for i, step in enumerate(scaleOrder):
            n = note.new(scale[i].name, scale[i].accidental)
            n.transpose(step)
            scale.append(n)

        return scale

    def render(self):

        if self.degree != '2' and self.degree != '3':
            degree = self.degree + 'th'
        elif self.degree == '2':
            degree = self.degree + 'nd'
        elif self.degree == '3':
            degree = self.degree + 'rd'

        rendered = self.tonic.render() + ' ' + self.name + ' scale' 
        rendered += ' in the ' + degree + ' degree \n'

        for i, n in enumerate(self.getScale()):
            if i == 0:
                rendered += n.render()
            else:
                rendered += ' - ' + n.render() 

        return rendered

def new(tonic, name, degree = 1):
    return Scale(tonic, name, degree)
    
