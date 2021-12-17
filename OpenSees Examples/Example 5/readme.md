# OpenSees Example 5. 2D Frame, 3-story 3-bay

This is an attempt to create [OpenSees Example 5](https://opensees.berkeley.edu/wiki/index.php/OpenSees_Example_5._2D_Frame,_3-story_3-bay,_Reinforced-Concrete_Section_%26_Steel_W-Section) in Python Interpreter.

![Example5_figure1](https://user-images.githubusercontent.com/54548261/146332935-694b8758-3aa8-4b97-a389-77531c47bf77.GIF)<br/>
Figure 1. Illustration of the 2D frame with node and element numbering and section assignment (Source: (c) [OpenSees](https://opensees.berkeley.edu/)).<br/>
Note that the “LCol” parameter has changed to “colHeight,” and the “LBeam” parameter has changed to “beamLength.”

## 2D Frame, 3-story 3-bay, Steel W-Section

### Distributed Plasticity Element—Fiber Section
![ExampleFigure_FiberSection_W](https://user-images.githubusercontent.com/54548261/146336212-cf7a92b7-a0c9-433e-92b7-e3cebcc1fafe.GIF)<br/>
Figure 2. Standard W section (Source: (c) [OpenSees](https://opensees.berkeley.edu/)).<br/>

Sections:
- Section A-A: W27x114
- Section B-B: W24x94

### Files
- [Ex5.Frame2D.InelasticFiberWSection.build.py](https://github.com/farshadrasuli/OpenSeesPy/blob/10f3f99a55837d43925c599012a194b3f8b18073/OpenSees%20Examples/Example%205/Ex5.Frame2D.InelasticFiberWSection.build.py) — Build model, and gravitational analysis.
- [LibUnits.py](https://github.com/farshadrasuli/OpenSeesPy/blob/10f3f99a55837d43925c599012a194b3f8b18073/OpenSees%20Examples/Example%205/LibUnits.py) — A module for units.
- [Wsection.py](https://github.com/farshadrasuli/OpenSeesPy/blob/10f3f99a55837d43925c599012a194b3f8b18073/OpenSees%20Examples/Example%205/Wsection.py) — A module for constructing a standard W- or I- shape Fiber Section object.
- [Ex5.Frame2D.InelasticFiberWSection.analyze.Static.Push.py](https://github.com/farshadrasuli/OpenSeesPy/blob/10f3f99a55837d43925c599012a194b3f8b18073/OpenSees%20Examples/Example%205/Ex5.Frame2D.InelasticFiberWSection.analyze.Static.Push.py) — Build model, gravitational analysis, and Static Push-over analysis.
