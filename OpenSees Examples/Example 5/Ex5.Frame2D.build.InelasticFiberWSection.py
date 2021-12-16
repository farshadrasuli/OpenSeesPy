# -----------------------------------------------------------------------------
# Example 5. 2D Frame --  Build Model
# nonlinearBeamColumn element, inelastic fiber section -- Steel W-Section
#		Silvia Mazzoni & Frank McKenna, 2006
#
#     This file provided by (c) Farshad Rasuli, 2021.
#
# E-Mail: farshad.rasuli@gmail.com
# github.com/farshadrasuli/OpenSeesPy/tree/main/OpenSees%20Examples/Example%205
# farshadrasuli.github.io/OpenSeesPy
# -----------------------------------------------------------------------------

# import the OpenSeesPy module
import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv
# import other modules
import os
import math
import matplotlib.pyplot as plt
# import auxiliary *.py files
import LibUnits as unit
import Wsection as Wsection










# Set up ======================================================================

# remove existing model
ops.wipe()


# modelbuilder
ops.model('basic', '-ndm', 2, '-ndf', 3)


# set up name of data directory (you can remove this)
dataDir = 'Data'
# create data directory
if not os.path.exists(dataDir):
    os.makedirs(dataDir)

# ground-motion file directory
GMDir = 'Ground-motions'
# create directory
if not os.path.exists(GMDir):
    os.makedirs(GMDir)

    








# Model generation ============================================================

# define structure-geometry paramters
colHeight = 14*unit.ft	# column height
beamLength = 24*unit.ft	# beam length

# calculate locations of beam/column intersections:
X1 = 0.
X2 = X1 + beamLength
X3 = X2 + beamLength
X4 = X3 + beamLength
Y1 = 0.
Y2 = Y1 + colHeight
Y3 = Y2 + colHeight
Y4 = Y3 + colHeight

# create nodes ································································
#         nodeTag,  X,  Y
ops.node(      11, X1, Y1)
ops.node(      12, X2, Y1)
ops.node(      13, X3, Y1)
ops.node(      14, X4, Y1)
ops.node(      21, X1, Y2)
ops.node(      22, X2, Y2)
ops.node(      23, X3, Y2)
ops.node(      24, X4, Y2)
ops.node(      31, X1, Y3)
ops.node(      32, X2, Y3)
ops.node(      33, X3, Y3)
ops.node(      34, X4, Y3)
ops.node(      41, X1, Y4)
ops.node(      42, X2, Y4)
ops.node(      43, X3, Y4)
ops.node(      44, X4, Y4)

# Set up parameters that are particular to the model for displacement control ·
tagCtrlNode = 41		# node where displacement is read for displacement control
tagCtrlDOF = 1	     	# degree of freedom of displacement read for displacement control
numStory = 3	       	# number of stories above ground level
numBay = 3	         	# number of bays
buildingHeight = Y4		# total building height

# set boundary condition ······················································
#        nodeTag, X, Y, RZ
ops.fix(      11, 1, 1,  0)
ops.fix(      12, 1, 1,  0)
ops.fix(      13, 1, 1,  0)
ops.fix(      14, 1, 1,  0)

# define materials ····························································

# Hardening Material
matHardening = 1
Es = 29000*unit.ksi		# tangent stiffness
Fy = 60.0*unit.ksi      # yield stress or force
nu = 0.3                # Poisson's ratio
Gs = Es/(2*(1+nu))      # Torsional stiffness Modulus
H_iso = 0.0             # isotropic hardening Modulus
H_kin = 1.e3            # kinematic hardening Modulus
eta = 0.                # visco-plastic coefficient
#                           Type,       matTag,  E, sigmaY, H_iso, H_kin, eta
ops.uniaxialMaterial("Hardening", matHardening, Es,     Fy, H_iso, H_kin, eta)

# define sections ·····························································

# sections: W27x114
secW27_114 = 1          # assign a tag number to the column section tag
d = 27.29*unit.inch 	# depth
bf = 10.07*unit.inch	# flange width
tf = 0.93*unit.inch 	# flange thickness
tw = 0.57*unit.inch 	# web thickness
nfdw = 16		# number of fibers along dw
nftw = 2		# number of fibers along tw
nfbf = 16		# number of fibers along bf
nftf = 4		# number of fibers along tf
#                     secTag,       matTag, d, bf, tf, tw, nfdw, nftw, nfbf, nftf
Wsection.section(secW27_114, matHardening, d, bf, tf, tw, nfdw, nftw, nfbf, nftf)

# sections: W24x94
secW24_94 = 4           # assign a tag number to the beam section tag
d = 24.31*unit.inch     # depth
bf = 9.065*unit.inch	# flange width
tf = 0.875*unit.inch	# flange thickness
tw = 0.515*unit.inch	# web thickness
nfdw = 16		# number of fibers along dw
nftw = 2		# number of fibers along tw
nfbf = 16		# number of fibers along bf
nftf = 4		# number of fibers along tf
#                    secTag,       matTag, d, bf, tf, tw, nfdw, nftw, nfbf, nftf
Wsection.section(secW24_94, matHardening, d, bf, tf, tw, nfdw, nftw, nfbf, nftf)

# set up geometric transformations of element ·································
colTransf = 1
beamTransf = 2
#              transfType,  transfTag
ops.geomTransf(  'Linear',  colTransf) # set P-Delta in case of P-Delta analysis for columns
ops.geomTransf(  'Linear', beamTransf)

# define elements ·····························································

numIntgrPts = 5	# number of Gauss integration points for nonlinear curvature distribution---np=2 for linear distribution ok

# columns
# level 1-2               eleType, eleTag, iNode, jNode, numIntgrPts,     secTag, transfTag
ops.element('nonlinearBeamColumn',    111,    11,    21, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    112,    12,    22, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    113,    13,    23, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    114,    14,    24, numIntgrPts, secW27_114, colTransf)
# level 2-3               eleType, eleTag, iNode, jNode, numIntgrPts,     secTag, transfTag
ops.element('nonlinearBeamColumn',    121,    21,    31, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    122,    22,    32, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    123,    23,    33, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    124,    24,    34, numIntgrPts, secW27_114, colTransf)
# level 3-4               eleType, eleTag, iNode, jNode, numIntgrPts,     secTag, transfTag
ops.element('nonlinearBeamColumn',    131,    31,    41, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    132,    32,    42, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    133,    33,    43, numIntgrPts, secW27_114, colTransf)
ops.element('nonlinearBeamColumn',    134,    34,    44, numIntgrPts, secW27_114, colTransf)

# beams
# level 2                 eleType, eleTag, iNode, jNode, numIntgrPts,     secTag, transfTag
ops.element('nonlinearBeamColumn',    221,    21,    22, numIntgrPts,  secW24_94, beamTransf)
ops.element('nonlinearBeamColumn',    222,    22,    23, numIntgrPts,  secW24_94, beamTransf)
ops.element('nonlinearBeamColumn',    223,    23,    24, numIntgrPts,  secW24_94, beamTransf)
# level 3                 eleType, eleTag, iNode, jNode, numIntgrPts,     secTag, transfTag
ops.element('nonlinearBeamColumn',    231,    31,    32, numIntgrPts,  secW24_94, beamTransf)
ops.element('nonlinearBeamColumn',    232,    32,    33, numIntgrPts,  secW24_94, beamTransf)
ops.element('nonlinearBeamColumn',    233,    33,    34, numIntgrPts,  secW24_94, beamTransf)
# level 4                 eleType, eleTag, iNode, jNode, numIntgrPts,     secTag, transfTag
ops.element('nonlinearBeamColumn',    241,    41,    42, numIntgrPts,  secW24_94, beamTransf)
ops.element('nonlinearBeamColumn',    242,    42,    43, numIntgrPts,  secW24_94, beamTransf)
ops.element('nonlinearBeamColumn',    243,    43,    44, numIntgrPts,  secW24_94, beamTransf)

# Render the model ····························································
opsv.plot_model()
plt.savefig('Model.png')










# Gravity Loads, weight, and masses ===========================================

# calculate dead load of frame, assume this to be an internal frame ···········
    # calculate distributed weight along the beam length
GammaConcrete = 150*unit.pcf    	# Reinforced-Concrete floor slabs
tSlab = 6*unit.inch	    	       	# 6-inch slab
lSlab= 2*beamLength/2  		    	# assume slab extends a distance of 1/2beamLength in/out of plane
slabWeight = GammaConcrete*tSlab*lSlab 
beamWeight = 94*unit.lbf/unit.ft	# W-section weight per length
beamDl = slabWeight + beamWeight  	# dead load distributed along beam.
colWeight = 114*unit.lbf/unit.ft   	# W-section weight per length

totColWeight = colWeight*colHeight 	# total Column weight
totBeamWeight = beamDl*beamLength  	# total Beam weight

# assign masses to the nodes that the columns are connected to ················

# each connection takes the mass of 1/2 of each element framing into it (mass=weight/$g)
# level 2
ops.mass(21, (totColWeight/2 + totColWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(22, (totColWeight/2 + totColWeight/2 +totBeamWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(23, (totColWeight/2 + totColWeight/2 +totBeamWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(24, (totColWeight/2 + totColWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
# level 3
ops.mass(31, (totColWeight/2 + totColWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(32, (totColWeight/2 + totColWeight/2 +totBeamWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(33, (totColWeight/2 + totColWeight/2 +totBeamWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(34, (totColWeight/2 + totColWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
# level 4
ops.mass(41, (totColWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(42, (totColWeight/2 +totBeamWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(43, (totColWeight/2 +totBeamWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)
ops.mass(44, (totColWeight/2 +totBeamWeight/2)/unit.g, 0., 0.)

# calculate total Floor Mass ··················································

# weight of each level
floorWeight2 = totColWeight*4/2 +totColWeight*4/2 +3*totBeamWeight
floorWeight3 = totColWeight*4/2 +totColWeight*4/2 +3*totBeamWeight
floorWeight4 = totColWeight*4/2 +3*totBeamWeight
# total frame weight
totalWeight = floorWeight2 + floorWeight3 + floorWeight4

# mass of each level
floorMass2 = floorWeight2/unit.g
floorMass3 = floorWeight3/unit.g
floorMass4 = floorWeight4/unit.g
# total frame mass
totalMass = floorMass2 + floorMass3 + floorMass4










# LATERAL-LOAD distribution for static pushover analysis ======================

# calculate distribution of lateral load based on mass/weight distributions along building height
# Fj = ( WjHj/sum(WiHi) ) * totalWeight   at each floor j

sumWiHi = floorWeight2*Y2 + floorWeight3*Y3 + floorWeight4*Y4 # denominator

Fj2 = floorWeight2*Y2/sumWiHi*totalWeight # total for floor 2
Fj3 = floorWeight3*Y3/sumWiHi*totalWeight # total for floor 3
Fj4 = floorWeight4*Y4/sumWiHi*totalWeight # total for floor 4

# per node at each floor j
Fi2 = Fj2/4			# per node on floor 2
Fi3 = Fj3/4			# per node on floor 3
Fi4 = Fj4/4			# per node on floor 4










# Eigen value analysis ========================================================

#                                       solver, numEigenvalues
squareEigenValues = ops.eigen('-fullGenLapack',     numStory*3)

# eigen values for each mode
eigenValues = [None] * len(squareEigenValues)
for i in range(len(squareEigenValues)):
    eigenValues[i] = math.sqrt(squareEigenValues[i]) # rad/sec

# period for each mode
T = [None] * len(eigenValues)
for i in range(len(eigenValues)):
    T[i] = 2.0 * math.pi / eigenValues[i] # sec










# Set recorders ==============================================================

# displacements of free node
ops.recorder('Node','-file', dataDir+'/freeNodeDisp.out', '-time', '-node', 41, '-dof', 1, 2, 3, 'disp')

# displacements of support nodes
ops.recorder('Node','-file', dataDir+'/baseDisp.out', '-time', '-node', 11, 12, 13, 14, '-dof', 1, 2, 3, 'disp')

# support reaction
ops.recorder('Node','-file', dataDir+'/baseReaction.out', '-time', '-node', 11, 12, 13, 14, '-dof', 1, 2, 3, 'reaction')

# lateral drift
#ops.recorder('Drift','-file', dataDir+'/DrNode.out', '-time', '-iNode', 11, '-jNode', 41, '-dof', 1, '-perpDirn', 2)

# forces in local coordinates, element i
ops.recorder('Element','-file', dataDir+'/ele111Forces.out', '-time', '-ele', 111, 'localForce')

# section forces, axial and moment, node i
ops.recorder('Element','-file', dataDir+'/ele111Sec1Force.out', '-time', '-ele', 111, 'section', 1, 'force')

# section deformations, axial and curvature, node i
ops.recorder('Element','-file', dataDir+'/ele111Sec1Defo.out', '-time', '-ele', 111, 'section', 1, 'deformation')

# section forces, axial and moment, node j
ops.recorder('Element','-file', dataDir+'/ele111Sec'+str(numIntgrPts)+'Force.out', '-time', '-ele', 111, 'section', numIntgrPts, 'force')

# section deformations, axial and curvature, node j
ops.recorder('Element','-file', dataDir+'/ele111Sec'+str(numIntgrPts)+'Defo.out', '-time', '-ele', 111, 'section', numIntgrPts, 'deformation')

# steel fiber stress-strain, node i
ops.recorder('Element','-file', dataDir+'/ele1sec1StressStrain.out', '-time', '-ele', 111, 'section', numIntgrPts, 'fiber', 0, 0, matHardening, 'stressStrain')










# Gravitational loading =======================================================

# set time series ·····························································
#                tsType, tag, '-factor', factor=1.0, '-tStart', tStart=0.0
ops.timeSeries('Linear',   1)


# set load pattern ····························································
#            patternType, patternTag, tsTag, '-fact', factor
ops.pattern(     'Plain',          1,     1)


# define gravity loads ························································

# beams (in -ydirection)
ops.eleLoad('-ele', 221, 222, 223, '-type', '-beamUniform', -beamDl)
ops.eleLoad('-ele', 231, 232, 233, '-type', '-beamUniform', -beamDl) 
ops.eleLoad('-ele', 241, 242, 243, '-type', '-beamUniform', -beamDl)

# columns (in -xdirection)
ops.eleLoad('-ele', 111, 112, 113, 114, '-type', '-beamUniform', 0, -colWeight)
ops.eleLoad('-ele', 121, 122, 123, 124, '-type', '-beamUniform', 0, -colWeight) 
ops.eleLoad('-ele', 131, 132, 133, 134, '-type', '-beamUniform', 0, -colWeight) 










# Gravity-analysis  parameters -- load-controlled static analysis =============

# convergence tolerance for test
tol = 1.0e-8

# set constraint---how it handles boundary conditions
ops.constraints('Plain') # large model with rigid diaphragm try Transformation

# set numberer---renumber dof's to minimize band-width (optimization), if you want to
ops.numberer('RCM')

# set the system of equation---how to store and solve the system of equations in the analysis (large model: try UmfPack)
ops.system('BandGen')

# set the test of equations---determine if convergence has been achieved at the end of an iteration step
ops.test('NormDispIncr', tol, 6)

# set algorithm---use Newton's solution algorithm: updates tangent stiffness at every iteration
ops.algorithm('Newton')

# define steps of analysis
numStepsGravity = 10                # define number of steps to apply gravity
gravityIncr = 1./numStepsGravity    # first load increment

# set integrator---determine the next time step for an analysis
ops.integrator('LoadControl', gravityIncr)

# set analysis---define type of analysis static or transient
ops.analysis('Static')

# do analysis---apply gravity
ops.analyze(numStepsGravity)

# Set the gravity loads to be constant & reset the time in the domain
ops.loadConst('-time', 0.0)










# Close the program ===========================================================
ops.wipe()
