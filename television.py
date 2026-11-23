class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        #set all our variables
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self):
        # thank you not keyword for making this way faster
        # it just switches it
        self.__status = not self.__status
    def mute(self):
        # if the power is on, it switches the mute command. does nothing otherwise
        if self.__status:
            self.__muted = not (self.__muted)


    def channel_up(self):
        #first, we check if the power's on
        if self.__status:
            # if the channel is at max, it goes to min
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                # otherwise, it increments
                self.__channel = self.__channel + 1

    def channel_down(self):
        if self.__status:
                # basic logic is the same here, except we go from min to max and decrement in general
                if self.__channel == Television.MIN_CHANNEL:
                    self.__channel = Television.MAX_CHANNEL
                else:
                    self.__channel = self.__channel - 1

    def volume_up(self):
        #of course, always check da power
        if self.__status:
            #first we check if we're muted, and if we are, unmute
            if self.__muted:
                self.mute()
                # then of course, we set the volume to increment, but ONLY if we're below the maximum volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self):
        # here, we start by making a volume keyword
        vol = 0
        # if we're unmuted, we set it to the volume variable. otherwise, it just stays at 0
        if not(self.__muted):
            vol = self.__volume
        #and of course we return our final string
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {vol}"