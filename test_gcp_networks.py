import ipaddress
#https://docs.python.org/3/howto/ipaddress.html
#https://docs.python.org/3/library/ipaddress.html


# List of GCP networks to avoid
gcp_networks_to_avoid =\
['10.100.0.0/14',
'10.104.0.0/20',
'10.28.0.0/14',
'10.32.0.0/20',
'10.48.0.0/20',
'10.44.0.0/14',
'10.128.0.0/14',
'10.132.0.0/20',
'10.72.0.0/20',
'10.68.0.0/14',
'10.140.0.0/14',
'10.144.0.0/20',
'10.196.0.0/14',
'10.200.0.0/20',
'10.40.0.0/14',
'10.48.16.0/20',
'10.24.0.0/14',
'10.21.128.0/20']


# candidate CIDR blocks to be tested if they exist within GCP networks to avoid
candidate_networks = ['10.21.0.0/23', '172.16.140.0/23']

for network_to_test in candidate_networks:
    print(f"****** Testing {network_to_test} ******")
    test_network = ipaddress.ip_network(network_to_test)

    for gcp_exclusion_network in gcp_networks_to_avoid:
        gcp_network = ipaddress.ip_network(gcp_exclusion_network)
        result = test_network.overlaps(gcp_network)
        print(f"{test_network} is in {gcp_network} : {result}")
