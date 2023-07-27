from UI import TC01_Register_001, TC02_Register_002, TC03_Register_003, TC04_Register_004, TC05_Register_005, TC06_Register_006, TC07_Register_007, TC08_Login_001, TC09_Login_002, TC10_Login_003

class UISuite():
    test_cases = []

    def __init__(self):
        self.test_cases.extend((TC01_Register_001.Test(), TC02_Register_002.Test(), TC03_Register_003.Test(), TC04_Register_004.Test(), TC05_Register_005.Test(), TC06_Register_006.Test(), TC07_Register_007.Test(), TC08_Login_001.Test(), TC09_Login_002.Test(), TC10_Login_003.Test()))

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
        print("✎  UI Suite finished successfully, final results: ")
        print(f"    Total tests ➳  {str(totalTests)}")
        print(f"    Tests Passed ➳  {str(testsPassed)}")
        print(f"    Tests Failed ➳  {str(testsFailed)}")
        print(" ")
        print(" You can check the logs file for more details about the execution.")
        print(" ")
        print("**=====================================================**")
        print("\n\n")

suite = UISuite()
suite.startSuite()