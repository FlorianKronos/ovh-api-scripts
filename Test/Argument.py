from optparse import OptionParser
def main():
    usage = "usage: %prog -n nic0000-OVH -u 'URL'"
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url",type="string",
                  help="Url Received y E-Mial from OVH")
    parser.add_option("-n", "--nic-handle", dest="nic",type="string",
                  help="Put your NIC-HANDLE OVH for API connection")
    (options, args) = parser.parse_args()
    if args !=1:
        parser.error("No URL")
    
if __name__ == "__main__":
    main()