#!/usr/bin/python

import pdb
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

setLogLevel ( 'info' )


def Topology():
	net = Mininet(controller= Cotroller, switch = OVSSwitch)
	
	print "******** Creating controller"
	c1= net.addController ('c1', ip='127.0.0.1', port = 6633)
	
	print "******** Creating switches"
	s1 = net.addSwitch( 's1' )
	s2 = net.addSwitch( 's2' )

	print "******** Creating host"
	h1 = net.addHost( 'h1' )
	h2 = net.addHost( 'h2' )
	
	print "******** Creating links"
	net.addLink (h1,s1)
	net.addLink (h2,s2)
	net.addLink (s1,s2)

	print "******* Starting network"
	net.build()
	c1.start
	s1.start([c1])
	s2.start([c2])
	
	net.start()

	print "******* Testing network"
	net.pingAll()

	print "****** Running CLI"
	CLI(net)
	
