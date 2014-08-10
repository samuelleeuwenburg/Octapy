# -*- coding: utf-8 -*-

import output

class Note:

    def __init__(self, name = 'C', accidental = False):
        self.name = name
        self.accidental = accidental

        if accidental != '#' and accidental != 'b' and accidental != 'x' and accidental != 'bb' and accidental != False:
            print 'error: ' + str(accidental) + ' is not a valid accidental'
            self.accidental = False

        self.note_values = {
            'C': 0.5,
            'D': 1.0,
            'E': 1.0,
            'F': 0.5,
            'G': 1.0,
            'A': 1.0,
            'B': 1.0
        }
        self.note_order = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

        try:
            self.note_values[self.name]
        except KeyError, e:
            output.warning(self.name + ' is not a valid note, will use C instead')
            self.name = 'C'

        self.step_value = self.note_values[self.name]

    def findRelativeAccidental(self):
        ''' TODO '''
        return self

    def transpose(self, steps):
        # set note order index starting from the note
        index = self.note_order.index(self.name) 
        head = self.note_order[0:index]
        tail = self.note_order[index:len(self.note_order)]
        self.note_order = tail + head

        # determine how many steps our note is
        cur_steps = self.note_values[self.name]
        # determine how many steps the next note is
        next_steps = self.note_values[self.note_order[1]]

        # set accidentals
        # if next item is a semitone away
        if next_steps == 0.5:
            # if the jump is a wholetone
            if steps == 1.0:
                if self.accidental == '#':
                    self.accidental = 'x'
                    
                elif self.accidental == False:
                    self.accidental = '#'

                elif self.accidental == 'b':
                    self.accidental = False

                elif self.accidental == 'bb':
                    self.accidental = 'b'
                    
            # if the jump is whole and a half
            if steps == 1.5:
                if self.accidental == 'bb':
                    self.accidental = False
                if self.accidental == 'b':
                    self.accidental = '#' 
                elif self.accidental == False:
                    self.accidental = 'x'

        # if next item is a wholestep away
        if next_steps == 1.0:
            # if the jump is a semitone 
            if steps == 0.5:
                if self.accidental == 'x':
                    self.accidental = '#'

                elif self.accidental == '#':
                    self.accidental = False

                elif self.accidental == False:
                    self.accidental = 'b'

                elif self.accidental == 'b':
                    self.accidental = 'bb' 
                    
            # if the jump is whole and a half
            if steps == 1.5:
                if self.accidental == 'bb':
                    self.accidental = 'b'
                if self.accidental == 'b':
                    self.accidental = False
                elif self.accidental == False:
                    self.accidental = '#'
                elif self.accidental == '#':
                    self.accidental = 'x'
                
        # jump 
        self.name = self.note_order[1]
        return self.render()

    def render(self):
        if self.accidental:
            accidental = self.accidental.replace('#', '♯')
            accidental = accidental.replace('b', '♭')
            accidental = accidental.replace('x', '𝄪')
            return self.name + accidental
        else:
            return self.name


    # Accidentals
    def flatten(self):
        self.accidental = 'b'

    def sharpen(self):
        self.accidental = '#'

    def naturalize(self):
        self.accidental = False


def new(name = 'C', accidental = False):
    return Note(name, accidental)

