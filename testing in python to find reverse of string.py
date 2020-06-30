import unittest
def reverse(self):
    a=input("Enter your string:")
    print("Reverse of string:")
    return(a[::-1])
class simpletest(unittest.TestCase):
    def testreverse(self):
        self.assertEquals(reverse("hello"),"olleh")
if __name__=='__main__':
    unittest.main()
