# VREP Synchronous Py-based External Client App

<p> Check port number for a correct socket communication between controller and server: </p>
<ol>
<li>Go to C:\Program Files\V-REP3\V-REP_PRO_EDU\remoteApiConnections.txt</li>
<li>Check port number: portIndex1_port = 19997</li>
<li>You will need this number on your controller's script.</li>
</ol>

<p>Make sure you have following files in the same directory where your controller is located:</p>
<ul>
<li>vrep.py</li>
<li>vrepConst.py</li>
<li>the appropriate remote API library: "remoteApi.dll" (Windows), "remoteApi.dylib" (Mac) or "remoteApi.so" (Linux)</li>
</ul>
<p>These files can be found in C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\python.</p>

<p>Open your simulation scene in VREP.</p>

<p>Run your_script.py (controller's script). The simulation will start automatically.</p>