# -*- coding: utf-8 -*-

import note
import scale 
import json 

class Chord:
    ''' Build a chord by passing a mode with chord position or chord name '''

    def __init__(self, root, name):
        self.root = root
        self.notes = self.buildChord(name)

    def getChord(self):
        ''' Return chord notes as an array '''
        return self.notes

    def getRoot(self):
        return root
        
    def buildChord(self, name):
        f = open('./patterns/chords.json')
        chords = json.loads(f.read())
        f.close()

        # build matching scale
        chordScale = scale.new(
            self.root, 
            chords[name]['scale'],
            chords[name]['degree']
        )

        chord = []

        for pos in chords[name]['degrees']:
            
            chord.append(chordScale.scale[pos - 1])

        return chord 


def new(root, name):
    return Chord(root, name) 


