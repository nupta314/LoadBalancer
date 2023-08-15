# LoadBalancer

This is the implementation of the task given in the 3 hr coding round for an Placement Oppurtunity .

The task had following parts:
    1.Implement a simple get/put/delete server  
    2.Implement a load balancer  
    3.Add persistence  
    4.(Bonus) Generalize the load balancer for N servers  

3 of the 4 parts have been implemented. This is also what I did in that round.

The Running order is psrv1.py psrv2.py plb.py pclient.py

The basic explanation for the 4rth part has been given. I have not implemented the 4rth part because its testing will require writing more servers which I am too lazy to do.

Before running ensure that the ports in range 65400-65402 are free

Edit 1:
All 4 parts have been implemented using pnlb.py and pnsrv.x.py series of files
for example number of servers is N, then:
    1.make files pnsrv.x.py where x is 1 to N, copy paste exact contents from file pnsrv.py
    2.run servers pnsrv.x.py where x is 1 to N
    3.then edit the pnlb.py file to make n=N
    4.then run pnlb.py
    5.then run pclient.py

Note:
    1.Remember to give 2 seconds gap between consecutive commands because python is slow and will mess up.
    2.Do not run pnsrv.py, its not for running.
    3.Make sure port range 65400 to 65400+N is free.
