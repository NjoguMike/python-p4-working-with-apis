
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    schools = []
    programs = json.loads(self.get_programs())
    for program in programs:
      schools.append(program['agency'])
    return schools

# programs = GetPrograms().get_programs()
programs = GetPrograms()
school_list = set(programs.program_school())

for school in school_list:
  print(school)