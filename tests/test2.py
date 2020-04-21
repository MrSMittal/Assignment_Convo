#test 2 where search is done by duration

import unittest
import urllib.request as req
import json

class Test(unittest.TestCase):
    def Test1(self):
        field_name='duration'
        value='120'
        url=f'http://localhost:4444/api?field_name={field_name}&value={value}'
        result = json.load(req.urlopen(url))
        expected={
          "Title": "Star Wars: Eine neue Hoffnung",
          "Plot": "Der im Exil lebende Jedi-Ritter Obi-Wan Kenobi nimmt sich einen Mann namens Luke Skywalker als Sch\u00c3\u00bcler. Zusammen helfen sie der Rebellion, die Pl\u00c3\u00a4ne des b\u00c3\u00b6sen Imperiums und des Sith-Lords Darth Vader zu vereiteln. ",
          "duration": 120,
          "Ratings": {
               "Source": "userrating",
               "Values": {
                    "countStar1": 5,
                    "countStar2": 3,
                    "countStar3": 88,
                    "countStar4": 101,
                    "countStar5": 417,
                    "countTotal": 614
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