from typing import List
from Src.kgdd.kg_reader import KGReader
from Src.kgdd.kg_tester import KGTester
from Src.kgdd.logger import Logger
from Src.kgdd.test_file import TestFile
from Src.kgdd.test_file_parser import TestFileParser
from Src.kgdd.test import Test

if __name__ == "__main__":
    kgreader = KGReader()
    logger = Logger()
    test_file_parser = TestFileParser()
    kgtester = KGTester(kgreader,logger,test_file_parser)
    
    testfile : TestFile = test_file_parser.parse(".\ex_testbed.json")

    tests : List[Test] = testfile.get_tests()

    test1 = tests[0]

    path = 'C:\\Users\\colin\\Desktop\\DevWorkspace\\sonar2021_demo\\polifonia_places_etl\\kg\\versions\\polifonia-kg-places-0.0.2.ttl'

    kgtester.run_tests(path, ".\\testbed2.json")