import pigpio

class Motor_Ctrl:
    def __init__(self, mLeftA, mLeftB, mRightA, mRightB):
        pi = pigpio.pi()
        self.pi = pi
        self.mLeftA = mLeftA
        self.mLeftB = mLeftB
        self.mRightA = mRightA
        self.mRightB = mRightB

        self.pi.set_mode(self.mLeftA,pigpio.OUTPUT)
        self.pi.set_mode(self.mLeftB,pigpio.OUTPUT)
        self.pi.set_mode(self.mRightA,pigpio.OUTPUT)
        self.pi.set_mode(self.mRightB,pigpio.OUTPUT)

        self.pi.write(self.mLeftA,1)
        self.pi.write(self.mLeftB,1)
        self.pi.write(self.mRightA,1)
        self.pi.write(self.mRightB,1)

    def forward(self):
        self.pi.write(self.mLeftA,1)
        self.pi.write(self.mLeftB,0)
        self.pi.write(self.mRightA,1)
        self.pi.write(self.mRightB,0)

    def back(self):
        self.pi.write(self.mLeftA,0)
        self.pi.write(self.mLeftB,1)
        self.pi.write(self.mRightA,0)
        self.pi.write(self.mRightB,1)

    def stop(self):
        self.pi.write(self.mLeftA,1)
        self.pi.write(self.mLeftB,1)
        self.pi.write(self.mRightA,1)
        self.pi.write(self.mRightB,1)

    def left(self):
        self.pi.write(self.mLeftA,1)
        self.pi.write(self.mLeftB,0)
        self.pi.write(self.mRightA,0)
        self.pi.write(self.mRightB,1)

    def right(self):
        self.pi.write(self.mLeftA,0)
        self.pi.write(self.mLeftB,1)
        self.pi.write(self.mRightA,1)
        self.pi.write(self.mRightB,0)

