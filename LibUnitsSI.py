# -----------------------------------------------------------------------------
# LibUnits.py -- define system of units
#       (c) Farshad Rasuli, 2021
#
# E-Mail: farshad.rasuli@gmail.com
# github.com/farshadrasuli/OpenSeesPy/tree/main/OpenSees%20Examples/Example%205/
# farshadrasuli.github.io/OpenSeesPy
#
# Inspired from:
# LibUnits.tcl -- define system of units
#		Silvia Mazzoni & Frank McKenna, 2006
# -----------------------------------------------------------------------------

import math

# define UNITS
m = 1.0	    		# define basic units -- output units
N = 1.0 			# define basic units -- output units
sec = 1.0 			# define basic units -- output units
LunitTXT = "m"			# define basic-unit text for output
FunitTXT = "N"			# define basic-unit text for output
TunitTXT = "sec"		# define basic-unit text for output
inch = 0.0254*m			# define basic imperial units
kip = 4.45e3*N 			# define basic imperial units
# define engineering units
cm = 1.e-2*m                # centimeter, needed for displacement input in MultipleSupport excitation
mm = 1.e-3*m                # mili-meter
ft = 12*inch                # foot
Pa = N/math.pow(m,2)        # Newton per square meter
kPa = 1.e3*Pa               # kilo-Pascal or kilo-Newton per square meter
MPa = 1.0e6*Pa              # Mega-Pascal or Newton per square mili-meter
GPa = 1.0e9*Pa              # Giga-Pascal or kilo-Newton per square mili-meter
ksi = kip/math.pow(inch,2)  # kilo-pounds per square inch
psi = 1.e-3*ksi             # pounds per square inch
lbf = psi*inch*inch	    	# pounds force
pcf = lbf/math.pow(ft,3)   	# pounds per cubic foot
psf = lbf/math.pow(ft,3) 	# pounds per square foot
cm2 = cm*cm                 # cm^2
cm4 = cm*cm*cm*cm           # cm^4
mm2 = mm*mm                 # mm^2
mm4 = mm*mm*mm*mm           # mm^4
in2 = inch*inch     		# inch^2
in4 = inch*inch*inch*inch 	# inch^4
PI = 2*math.asin(1.0)   	# define constants
g = 9.80665*m/math.pow(sec,2)    	# gravitational acceleration
Ubig = 1.e10            			# a really large number
Usmall = 1/Ubig             		# a really small number
