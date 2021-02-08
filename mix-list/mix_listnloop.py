#!/usr/bin/env python3

def main():
    # below is a lists of lists containing the drivers needed to connect to
    # the switch IP addresses
    networklists = [['ios', '10.0.2.1'], ['ios', '10.0.55.1'], ['ios-xr', '10.0.3.1'], \
      ['junos', '10.0.10.1'], ['eos', '10.0.14.1']]
    #driveandip is each list in networklists and has the list values of the drive and ip eg. 'ios' and '10.0.2.1' 
    #driveandip[] the number inside the brackets are the list values of the driveandip
    #driveandip[1] = the ip address 
    #driveandip[0] = the driver
    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])
        
main()
