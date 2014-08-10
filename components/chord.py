# -*- coding: utf-8 -*-

import note
import scale 
import json 
import output

class Chord:
    ''' Build a chord by passing a name and tonic '''

    def __init__(self, root, name):
        self.root = root
        self.name = name
        self.notes = self.buildChord()

    def getChord(self):
        ''' Return chord notes as an array '''
        return self.notes

    def getRoot(self):
        return root
        
    def buildChord(self):
        f = open('./patterns/chords.json')
        chords = json.loads(f.read())
        f.close()

        try:
            chords[self.name]
        except KeyError, e:
            output.warning('Can\'t find a chord named ' + self.name + ', will use maj7 instead')
            self.name = 'maj7'

        # build matching scale
        chordScale = scale.new(
            self.root, 
            chords[self.name]['scale'],
            chords[self.name]['degree']
        )

        chord = []

        for pos in chords[self.name]['degrees']:
            
            chord.append(chordScale.scale[pos - 1])

        return chord 

    def render(self):

        rendered = self.root.render() + self.name + '\n'

        for i, n in enumerate(self.getChord()):
            if i == 0:
                rendered += n.render()
            else:
                rendered += ' - ' + n.render() 

        return rendered


def new(root, name):
    return Chord(root, name) 

