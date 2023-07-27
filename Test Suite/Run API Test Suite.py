from API import TC11_Register_001, TC12_Register_002, TC13_Register_003, TC14_Register_004, TC15_Register_005, TC16_Register_006, TC17_Register_007, TC18_Login_001, TC19_Login_002, TC20_Login_003


class APISuite():
    test_cases = []

    def __init__(self):
        self.test_cases.extend((TC11_Register_001.Test(), TC12_Register_002.Test(), TC13_Register_003.Test(), TC14_Register_004.Test(), TC15_Register_005.Test(), TC16_Register_006.Test(), TC17_Register_007.Test(), TC18_Login_001.Test(), TC19_Login_002.Test(), TC20_Login_003.Test()))
        
    def startSuite(self):
        totalTests = len(self.test_cases)
        testsPassed = 0
        testsFailed = 0

        for test in self.test_cases:
            result_data = test.startTest()

            if result_data["passed"]:
                testsPassed += 1
            else:
                testsFailed += 1

        print("\n\n")
        print("**=====================================================**")
        print(" ")
        print("⚡ API Suite finished successfully, final results: ")
        print(f"    Total tests ➳ {str(totalTests)}")
        print(f"    Tests Passed ➳ {str(testsPassed)}")
        print(f"    Tests Failed ➳ {str(testsFailed)}")
        print(" ")
        print(" You can check the logs file for more details about the execution.")
        print(" ")
        print("**=====================================================**")
        print("\n\n")


suite = APISuite()
suite.startSuite()