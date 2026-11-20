class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL
        # if i don't do it like this i think something breaks internally, you can try to figure out whats up but iont got any clue
        self.storeVolume = 0
    def power(self):
        # thank you not keyword(!) for making this way faster
        self.status = not (self.status)
    def mute(self):
        if self.status:
            self.muted = not (self.muted)
            if self.muted:
                self.storeVolume = self.volume
                self.volume = 0
            else:
                self.volume = self.storeVolume
                self.storeVolume = 0

    def channel_up(self):
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel = self.channel + 1

    def channel_down(self):
        if self.status:
                if self.channel == Television.MIN_CHANNEL:
                    self.channel = Television.MAX_CHANNEL
                else:
                    self.channel = self.channel - 1

    def volume_up(self):
        if self.status:
            self.mute()
            if self.volume < Television.MAX_VOLUME:
                self.volume = self.volume + 1

    def volume_down(self):
        if self.status:
            self.mute()
            if self.volume > Television.MIN_VOLUME:
                self.volume = self.volume - 1
# git is broken as fuck
    def __str__(self):
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"