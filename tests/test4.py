#test 4 where value is all lower case

import unittest
import urllib.request as req
import json

class Test(unittest.TestCase):
    def Test1(self):
        field_name='TITLE'
        value='das dschungelbuch'
        url=f'http://localhost:4444/api?field_name={field_name}&value={value}'
        result = json.load(req.urlopen(url))
        expected={
          "Title": "Das Dschungelbuch",
          "Plot": "Unter der Obhut des Panthers Baghira w\u00c3\u00a4chst das Findelkind Mogli bei einer Wolfsfamilie auf. Doch da ersch\u00c3\u00bcttert die R\u00c3\u00bcckkehr des menschenfressenden Tigers Shir Khan den Dschungel. Die Sorge um Mogli zwingt Baghira zu der einzig m\u00c3\u00b6glichen Entscheidung.",
          "duration": 75,
          "Ratings": {
               "Source": "userrating",
               "Values": {
                    "countStar1": 1,
                    "countStar2": 2,
                    "countStar3": 49,
                    "countStar4": 37,
                    "countStar5": 140,
                    "countTotal": 229
               }
          },
          "languages": [
               "de",
               "en"
          ]
     }
        
        self.assertEqual(expected,result)
        
if __name__ == '__main__':
        unittest.main()