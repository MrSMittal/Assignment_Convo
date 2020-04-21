#test 5 where value is not provided in the api call

import unittest
import urllib.request as req
import json

class Test(unittest.TestCase):
     def Test1(self):
          field_name='title'
          url=f'http://localhost:4444/api?field_name={field_name}'
          result = json.load(req.urlopen(url))
          expected={
          "Movie 1": {
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
          },
          "Movie 2": {
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
          },
          "Movie 3": {
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
          },
          "Movie 4": {
          "Title": "Sin City",
          "Plot": "Im S\u00c3\u00bcndenpfuhl Sin City werden drei Geschichten parallel erz\u00c3\u00a4hlt: Der Polizist Hartigan jagt einen P\u00c3\u00a4dophilen, der Outlaw Dwight muss im Rotlichtbezirk untertauchen und dem Schl\u00c3\u00a4ger Marv wird ein Mord angeh\u00c3\u00a4ngt. ",
          "duration": 119,
          "Ratings": {
          "Source": "userrating",
          "Values": {
          "countStar1": 169,
          "countStar2": 152,
          "countStar3": 751,
          "countStar4": 847,
          "countStar5": 1197,
          "countTotal": 3116
          }
          },
          "languages": [
          "de",
          "en"
          ]
          },
          "Movie 5": {
          "Title": "Indiana Jones und der letzte Kreuzzug",
          "Plot": "1912: Der junge Indiana Jones will Grabr\u00c3\u00a4ubern das Kreuz von Coronado abluchsen, um es in ein Museum zu bringen. Nach einem Zeitsprung ins Jahr 1938 k\u00c3\u00a4mpft Indy wieder um das Kreuz, diesmal erfolgreich. Anschlie\u00c3\u0178end soll er den Heiligen Gral suchen.",
          "duration": 127,
          "Ratings": {
          "Source": "userrating",
          "Values": {
          "countStar1": 20,
          "countStar2": 24,
          "countStar3": 1103,
          "countStar4": 1224,
          "countStar5": 2349,
          "countTotal": 4720
          }
          },
          "languages": [
          "de",
          "en"
          ]
          }
          }

          self.assertEqual(expected,result)
        
if __name__ == '__main__':
     unittest.main()