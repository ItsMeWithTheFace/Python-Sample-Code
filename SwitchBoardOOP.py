# Class 1
class LightSwitch():
    ''' A class to turn on and off a light switch.
    '''
    def __init__(self, switch_pos):
        ''' (LightSwitch, str) -> NoneType
        Creates a lightswitch that starts in a default state given either 'on'
        (True) or 'off' (False) as input

        REQ: switch_pos == 'on' or switch_pos == 'off'
        '''
        # Checks if input parameter is on or off then converts it into boolean
        if(switch_pos == 'on'):
            self._switch_pos = True
        elif(switch_pos == 'off'):
            self._switch_pos = False

    def turn_on(self):
        ''' (LightSwitch) -> NoneType
        Puts the lightswitch in the 'on' position (True)
        '''
        # Mutates _switch_pos to the 'on' state (True)
        self._switch_pos = True

    def turn_off(self):
        ''' (LightSwitch) -> NoneType
        Puts the lightswitch in the 'off' position (False)
        '''
        # Mutates _switch_pos to the 'off' state (False)
        self._switch_pos = False

    def flip(self):
        ''' (LightSwitch) -> NoneType
        Puts the lightswitch in the opposite position
        '''
        # Checks the state of _switch_pos and then switches it to the opposite
        # boolean value
        if(self._switch_pos is True):
            self._switch_pos = False
        else:
            self._switch_pos = True

    def __str__(self):
        ''' (LightSwitch) -> str
        Returns the state of the switch (either on or off)
        '''
        # Returns the state of the boolean as a string
        if(self._switch_pos is True):
            return ('I am on')
        else:
            return ('I am off')


# Class 2
class SwitchBoard():
    ''' A class representing a switchboard
    '''

    def __init__(self, num_switch):
        ''' (SwitchBoard, int) -> NoneType
        Sets the number of switches in the switchboard
        '''
        # Make an empty list
        self.switches = []
        # Add Nones to the list then switch them to LightSwitch objects in the
        # 'off' position
        for i in range(num_switch):
            self.switches.append(None)
            self.switches[i] = LightSwitch('off')

    def __str__(self):
        ''' (SwitchBoard) -> str
        Returns a list of the switches that are on
        '''
        # Create empty string
        on_switches = ''
        # Look through the list and add the positions containing an on switch
        # to the string
        for j in range(len(self.switches)):
            if(self.switches[j]._switch_pos is True):
                on_switches += (str(j) + " ")
        # Return the string of on switches
        return ('The following switches are on: ' + on_switches)

    def which_switch(self):
        ''' (SwitchBoard) -> int
        Returns a list of integers representing the switches that are on in
        order
        '''
        # Create a new list
        switches_on = []
        # Look through list of switches and add the 'on' switches to the new
        # list
        for k in range(len(self.switches)):
            if(self.switches[k]._switch_pos is True):
                switches_on.append(k)
        # Return list containing indexes of on switches
        return switches_on

    def flip(self, n):
        ''' (SwitchBoard, int) -> NoneType
        Flips the state of the nth lightswitch in the switchboard
        '''
        # Calls the flip method in LightSwitch to change the position of the
        # lightswitch at n
        if(n < len(self.switches)):
            self.switches[n].flip()

    def flip_every(self, n):
        ''' (SwitchBoard, int) -> NoneType
        Flips the state of every nth lightswitch in the switchboard
        '''
        # Calls the flip method in LightSwitch to flip every n lightswitch
        index = 0
        while(index < len(self.switches)):
            self.switches[index].flip()
            index += n

    def reset(self):
        ''' (SwitchBoard) -> NoneType
        Returns all the switches in the switchboard back to the 'off' position
        '''
        # Calls the turn_off method in LightSwitch for all the objects in the
        # switch_pos list
        for switch in self.switches:
            switch.turn_off()
