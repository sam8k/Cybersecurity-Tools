# @sam8k - 11/01/2021
# The code below accepts a pom.xml file
# And performs # ./dependencyManagement/dependencies/dependency search
# And prints all the groupId and versions

import xml.etree.ElementTree as ET
import optparse


# Function to extract the dependency
def extract(target, file):
    mytree = ET.parse(file)
    myroot = mytree.getroot()
    for x in myroot.findall(target):
        groupId = x.find('groupId').text
        version = x.find('version').text
        print(groupId, version)

# Input switches
parse = optparse.OptionParser()
parse.add_option("-t", "--target", dest="target", help="Enter the target hierarchy")
parse.add_option("-f", "--file", dest="file", help="Enter the target file")
(options, arguments) = parse.parse_args()
extract(options.target, options.file)



