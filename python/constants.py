import numpy as np

class hardware:
    def __init__(self):
        self.Rm = 250.0/2
        self.Rf = 650.0/2
        self.alpha = 40.0
        self.beta = 85.0

        # Vector from body center to hip joints, mm
        self.s = np.array( [ [ -55,0, 76.162, 0.0 ],        # Front left
                             [  55,0, 76.162, 0.0 ],        # Front right
                             [ -83.376, 0.0, 0.0 ],         # Middle left
                             [  83.376, 0.0, 0.0 ],         # Middle right
                             [ -55,0, -76.162, 0.0 ],       # Back left
                             [  55,0, -76.162, 0.0 ] ] )    # Back right

        # Leg link lengths, mm
        self.L1 = 32.26     # Coxa
        self.L2 = 90.0      # Femur
        self.L3 = 113.0     # Tibia

        # PWM channel for each motor
        self.legChannel = np.array( [ [ 16, 17, 18 ],       # Front left
                                      [ 15, 14, 13 ],       # Front right
                                      [ 19, 20, 21 ],       # Middle left
                                      [ 12, 11, 10 ],       # Middle right
                                      [ 22, 23, 27 ],       # Back left
                                      [  9,  8, 31 ] ] )    # Back right

        # Motor angle centers
        self.motorCenter = np.array( [  [ 115, 100, 160 ],
                                        [ 120, 105, 20 ],
                                        [ 120, 110, 155 ],
                                        [ 120, 110, 26 ],
                                        [ 100, 110, 143 ],
                                        [ 125, 120, 25 ] ] )

        # Motor angle mins
        self.motorMin = np.array( [ [ 50, 20, 0 ],
                                    [ 85, 10, 0 ],
                                    [ 70, 15, 0 ],
                                    [ 70, 15, 0 ],
                                    [ 60, 20, 0 ],
                                    [ 60, 20, 0 ] ] )

        # Motor angle maxs
        self.motorMax = np.array( [ [ 150, 180, 180 ],
                                    [ 175, 180, 180 ],
                                    [ 160, 180, 180 ],
                                    [ 170, 180, 180 ],
                                    [ 160, 180, 180 ],
                                    [ 165, 180, 180 ] ] )

        # Motor angle command matches matches defined orientation angle
        self.motorOrientation = np.array( [ [ -1, -1, -1 ],
                                            [ -1,  1,  1 ],
                                            [ -1, -1, -1 ],
                                            [ -1,  1,  1 ],
                                            [ -1, -1, -1 ],
                                            [ -1,  1,  1 ] ] )

                    

class channels:
    def __init__(self):
        self.desired_pose = 'desired_pose'
        self.leg_lengths = 'leg_lengths'


    