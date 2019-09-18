#quick test that works on my laptop
from cssi_cp2k.classes import SIM as sim

mySim = sim.SIM()

mySim.GLOBAL.RUN_TYPE = "MD"
mySim.GLOBAL.PROJECT  = "iodine-liquid"
mySim.GLOBAL.IO_LEVEL = "LOW"

mySim.MOTION.MD.ENSEMBLE = "NVT"
mySim.MOTION.MD.STEPS  = 1000000
mySim.MOTION.MD.TIMESTEP = 0.5
mySim.MOTION.MD.TEMPERATURE = 409.0
mySim.MOTION.MD.THERMOSTAT.TYPE = "NOSE"
mySim.MOTION.MD.THERMOSTAT.REGION = "MASSIVE"
mySim.MOTION.MD.THERMOSTAT.NOSE.LENGTH = 3
mySim.MOTION.MD.THERMOSTAT.NOSE.YOSHIDA = 3
mySim.MOTION.MD.THERMOSTAT.NOSE.TIMECON = 1000.0
mySim.MOTION.MD.THERMOSTAT.NOSE.MTS = 2
mySim.MOTION.MD.PRINT.ENERGY.EACH.MD = 20
mySim.MOTION.MD.PRINT.PROGRAM_RUN_INFO.EACH.MD = 20
mySim.MOTION.GEO_OPT.MAX_ITER= 2
#mySim.MOTION.MD.AVERAGES.SECTION_PARAMETERS= ".falbmbjse."

mySim.FORCE_EVAL.STRESS_TENSOR='ANALYTICAL';


mySim.MOTION.PRINT.FORCES.SECTION_PARAMETERS="ON"
mySim.MOTION.PRINT.RESTART_HISTORY.SECTION_PARAMETERS="DEBUG"
mySim.MOTION.PRINT.RESTART.SECTION_PARAMETERS="ON"

mySim.FORCE_EVAL.METHOD='QUICKSTEP'
mySim.FORCE_EVAL.DFT.BASIS_SET_FILE_NAME='dnsbdsbds'
mySim.FORCE_EVAL.DFT.QS.STO_NG=2
mySim.FORCE_EVAL.DFT.POISSON.PERIODIC="XYZ"
mySim.FORCE_EVAL.DFT.PRINT.E_DENSITY_CUBE.SECTION_PARAMETERS="ON"
mySim.FORCE_EVAL.DFT.SCF.OT.SECTION_PARAMETERS=".TRUE."
mySim.FORCE_EVAL.DFT.SCF.OT.ALGORITHM="IRAC"
mySim.FORCE_EVAL.DFT.SCF.PRINT.DM_RESTART_WRITE='.TRUE.'

mySim.FORCE_EVAL.DFT.XC.XC_FUNCTIONAL.SECTION_PARAMETERS='BLYP'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.POTENTIAL_TYPE='NONE'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.TYPE='DFTD3'
mySim.write_changeLog(fn="iodine-changeLog.out")
mySim.write_errorLog()
mySim.write_inputFile()
