import urllib.request as req
import json
import os
import cgi,cgitb

def notfound(environ,start_response):
    
    start_response('404 Not Found',[('Content-type','text/plain')])
    return [b'404 Not Found']

class PathDispatcher:
    def __init__(self):
        self.pathmap={}
    
    def __call__(self, environ,start_response):
        path=environ['PATH_INFO']
        params=cgi.FieldStorage(environ['wsgi.input'],environ=environ)
        method=environ['REQUEST_METHOD'].lower()
        environ['params']={k:params.getvalue(k) for k in params}
        handler=self.pathmap.get((method,path),notfound)
        return handler(environ,start_response)
    
    def register(self, method, path, function):
        self.pathmap[method.lower(),path] = function
        return function


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
            local_dictionary[f'Movie {counter}']['duration']=local_json_object['duration']
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
    
       
    #return 'Update Successfull'
    
    
def Search(feild='all',value='all'):
    print ('Method Ran')
    with open("masterbase.json", "r") as json_file: 
        local_json_object=json.load(json_file)
    
    if feild.lower() == 'all':
       if value == 'all':
           return local_json_object
       
    else:
        for id in local_json_object:
            for elem in  local_json_object[id]:
                if str(elem).lower()==str(feild).lower():
                    if str(local_json_object[id][elem]).lower()==str(value).lower():
                        return local_json_object[id]
                
                            




def MainMethod(environ,start_repsonse):
    start_repsonse('200 OK',[('Context-type','text/html')] )
    params=environ['params']
    print (params)
    reload()
    print(params)
    if len(params) == 2:
        final_output=str(Search(feild=params['field_name'],value=params['value']))
    else :
        final_output=str(Search())

    print (final_output)
    yield final_output.encode('utf-8')
    
    
if __name__ =='__main__':
    from wsgiref.simple_server import make_server
    
    dispatcher=PathDispatcher()
    dispatcher.register('GET','/api',MainMethod)
    httpd=make_server('localhost',4444,dispatcher)
    httpd.serve_forever()