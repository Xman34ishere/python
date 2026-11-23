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
    def power(self):
        # thank you not keyword for making this way faster
        self.status = not (self.status)
    def mute(self):
        if self.status:
            self.muted = not (self.muted)


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
            if self.muted:
                self.mute()
            if self.volume < Television.MAX_VOLUME:
                self.volume = self.volume + 1

    def volume_down(self):
        if self.status:
            if self.muted:
                self.mute()
            if self.volume > Television.MIN_VOLUME:
                self.volume = self.volume - 1

    def __str__(self):
        vol = 0
        if self.muted:
            vol = 0
        else:
            vol = self.volume
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {vol}"