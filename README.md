# BASIC SYNCHRONOUS PY-BASED EXTRENAL CLIENT APP FOR VREP 

Check port number for a correct socket communication between controller and server:
	1. Go to C:\Program Files\V-REP3\V-REP_PRO_EDU\remoteApiConnections.txt
	2. Check port number: 
		portIndex1_port             = 19997 <--!!
		portIndex1_debug            = true
		portIndex1_syncSimTrigger   = true 
	3. You will need this number on your controller's script. 

Make sure you have following files in the same directory where your controller is located:
	- vrep.py
	- vrepConst.py
	- the appropriate remote API library: "remoteApi.dll" (Windows), "remoteApi.dylib" (Mac) or "remoteApi.so" (Linux)
These files can be found in C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\python.

Open your simulation scene in VREP.

Run your_script.py (controller's script). The simulation will start automatically.