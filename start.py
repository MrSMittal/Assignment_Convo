import urllib.request as req
import json
from tkinter import * 
import os
from functools import partial  


#Update api key here
omdb_api='68fd98ab'

#Relative path 
path_to_local_json='movies'


omdb_access_query=f'http://www.omdbapi.com/?i=tt3896198&apikey={omdb_api}'

master_dictionary={}

def reload():
    local_dictionary={}
    counter=1
    omdb_json_object = json.load(req.urlopen(omdb_access_query))
    print(len(omdb_json_object))
    print (len(os.listdir(path_to_local_json)))
    local_dictionary['Movie 1']={}
    local_dictionary['Movie 1']['title']=omdb_json_object['Title']
    local_dictionary['Movie 1']['description']=omdb_json_object['Plot']
    local_dictionary['Movie 1']['duration']=omdb_json_object['Runtime']
    local_dictionary['Movie 1']['Ratings']=omdb_json_object['Ratings']
    local_dictionary['Movie 1']['Director']=[x for x in omdb_json_object['Director'].split(',')]
    local_dictionary['Movie 1']['Writer']=[x for x in omdb_json_object['Writer'].split(',')]
    local_dictionary['Movie 1']['Actors']=[x for x in omdb_json_object['Actors'].split(',')]
    local_dictionary['Movie 1']['languages']=[x for x in omdb_json_object['Language'].split(',')]
               
    for file in os.listdir(path_to_local_json):
        counter += 1
        with open('{}/{}'.format(path_to_local_json,file)) as json_file:
            local_json_object=json.load(json_file)
            local_dictionary[f'Movie {counter}']={}
            local_dictionary[f'Movie {counter}']['Title']=local_json_object['title']
            local_dictionary[f'Movie {counter}']['Plot']=local_json_object['description']
            local_dictionary[f'Movie {counter}']['Runtime']=local_json_object['duration']
            local_dictionary[f'Movie {counter}']['Ratings']={'Source':'userrating','Values':local_json_object['userrating']}
            if 'Director' in local_json_object.keys():
                local_dictionary[f'Movie {counter}']['Director']=[x for x in local_json_object['Director']]
            if 'Writer' in local_json_object.keys():
                local_dictionary[f'Movie {counter}']['Writer']=[x for x in local_json_object['Writer']]
            if 'Actors' in local_json_object:
                local_dictionary[f'Movie {counter}']['Actor']=[x for x in local_json_object['Actor']]
            local_dictionary[f'Movie {counter}']['languages']=[x for x in local_json_object['languages']]
    
    print(file)
    print(local_dictionary)
    with open("masterbase.json", "w") as outfile: 
        outfile.write(json.dumps(local_dictionary,indent=5)) 
    
    lbl3 = Label(window, text="Reload Successfull",   font=("Arial Bold", 10),fg='#0059b3')
    lbl3.grid(column=0, row=5)
    
    return 'Update Successfull'
    
    
def Search(feild='title',value='all'):
    with open("masterbase.json", "r") as json_file: 
        local_json_object=json.load(json_file)
    
    if feild == 'title':
       if value == 'all':
           lbl3 = Label(window, text=local_json_object,   font=("Arial Bold", 10),fg='green')
           lbl3.grid(column=0, row=5,)
           return local_json_object
       else:
           for id in local_json_object:
               if local_json_object[id]['title'].lower()==value.lower():
                   lbl3 = Label(window, text=local_json_object[id],font=("Arial Bold", 10),fg='green')
                   lbl3.grid(column=0, row=5,)
                   return local_json_object[id]
    else:
       if value == 'all':
           lbl3 = Label(window, text=local_json_object,   font=("Arial Bold", 10),fg='green')
           lbl3.grid(column=0, row=5,)
           return local_json_object
       else:
           for id in local_json_object:
               for elem in  local_json_object[id]:
                    if elem.lower()==feild.lower():
                        if local_json_object[id][elem].lower()==value.lower():
                            lbl3 = Label(window, text=local_json_object[id],font=("Arial Bold", 10),fg='green')
                            lbl3.grid(column=0, row=5,)
                            return local_json_object[id]
                        
                            
                  
    



window = Tk()
window.title("Welcome to the Movie Search Tool")

lbl = Label(window, text="Please Enter the movie to be searched below: ",   font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Please Enter which feild to be searched: ",   font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Please Enter which value to be searched: ",   font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)


searchFeild = Entry(window,width=70)
searchVAl = Entry(window,width=70)
searchFeild.grid(column=1, row=1)
searchVAl.grid(column=1, row=2)
print (searchFeild)

reload_btn = Button(window, text="Reload", command=reload)


search_btn=Button(window, text="Search", command=Search(searchFeild.get(),searchVAl.get()))


search_btn.grid(column=2,row=3)
reload_btn.grid(column=1, row=3)
window.mainloop()

print searchFeild.get()

