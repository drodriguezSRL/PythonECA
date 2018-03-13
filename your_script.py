#----------------------------------------------------------------------------------------------------------
# API Checklist:
# - Correct port number (19997) --> Check in C:\Program Files\V-REP3\V-REP_PRO_EDU\remoteApiConnections.txt
# - vrep.py, vrepConst.py, remoteApi.dll in directory
#----------------------------------------------------------------------------------------------------------
import vrep 
 
# Close any open communication threads with VREP (just in case)
vrep.simxFinish(-1)

# Starts a communication thread with the server (i.e. V-REP). 
# A same client may start several communication threads (but only one communication thread for a given IP and port).
# This should be the very first remote API function called on the client side. 
# Make sure to start an appropriate remote API server service on the server side, that will wait for a connection. 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 500, 5) 

if clientID != -1: # if we connected successfully
    print ('Connected to remote API server')
	# Remote API function calls will be executed asynchronously by default. 
	# We want to control the simulation progress so that VREP advances synchronously with our client app
	# This can be achieved by using the remote API synchronous mode:
	simxSynchronous(clientID, True) #Enable the synchronous mode 
	
	simxStartSimulation(clientID, vrep.simx_opmode_oneshot) #Start the simulation

	#-------------- ADD CONTROL LOOP HERE ------------------


	#-------------------------------------------------------
	# The simulation waits for a trigger before being moved ahead one time step:
	simxSynchronousTrigger(clientID) #Triggers next simulation step 
	
    # stop the simulation
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_blocking)

    # Before closing the connection to V-REP,
    # make sure that the last command sent out had time to arrive.
    vrep.simxGetPingTime(clientID)

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
    print('connection closed...')

else:
	raise Exception('Failed connecting to remote API server')