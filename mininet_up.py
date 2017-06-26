#!/usr/bin/python 

"""
Goal: To create an environment for ipop features.

Examples: Stun and Turn NAT Traversal testing and IPOP-Switch Mode
"""

import sys

from mininet.net import Mininet
from mininet.cli import CLI

def main():
    net = Mininet()

    s0 = net.addSwitch('s0')
    c0 = net.addController('c0')

    host1 = net.addHost('h1')
    host2 = net.addHost('h2')

    net.addLink(host1, s0)
    net.addLink(host2, s0)

    net.start()

    print host1.cmd('ping -c1', host2.IP())

    CLI(net)
    net.stop()

if __name__ == "__main__":
    main()
