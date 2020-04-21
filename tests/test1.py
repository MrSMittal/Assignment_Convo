import unittest
import urllib.request as req
import json
#test 1 Search by Movie Title

class Test(unittest.TestCase):
    def Test1(self):
        field_name='title'
        value='Guardians of the Galaxy Vol. 2'
        url=f'http://localhost:4444/api?field_name={field_name}&value={value}'
        result = json.load(req.urlopen(url))
        expected={
          "title": "Guardians of the Galaxy Vol. 2",
          "description": "The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father the ambitious celestial being Ego.",
          "duration": "136 min",
          "Ratings": [
               {
                    "Source": "Internet Movie Database",
                    "Value": "7.6/10"
               },
               {
                    "Source": "Rotten Tomatoes",
                    "Value": "85%"
               },
               {
                    "Source": "Metacritic",
                    "Value": "67/100"
               }
          ],
          "Director": [
               "James Gunn"
          ],
          "Writer": [
               "James Gunn",
               " Dan Abnett (based on the Marvel comics by)",
               " Andy Lanning (based on the Marvel comics by)",
               " Steve Englehart (Star-Lord created by)",
               " Steve Gan (Star-Lord created by)",
               " Jim Starlin (Gamora and Drax created by)",
               " Stan Lee (Groot created by)",
               " Larry Lieber (Groot created by)",
               " Jack Kirby (Groot created by)",
               " Bill Mantlo (Rocket Raccoon created by)",
               " Keith Giffen (Rocket Raccoon created by)",
               " Steve Gerber (Howard the Duck created by)",
               " Val Mayerik (Howard the Duck created by)"
          ],
          "Actors": [
               "Chris Pratt",
               " Zoe Saldana",
               " Dave Bautista",
               " Vin Diesel"
          ],
          "languages": [
               "English"
          ]
     }
        
        self.assertEqual(expected,result)
        
if __name__ == '__main__':
        unittest.main()