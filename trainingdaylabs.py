import requests

arch = ['Enterprise Networks','Datacenter','Collaboration','Security','Devnet','Meraki']

while True:
      for x in arch: 
          url = 'http://ec2-54-90-189-154.compute-1.amazonaws.com/api/labs/arch/' + x
          r = requests.get(url)

          if len(r.json()) == '0':
                    print ("Light Off!")
          if 1 <= len(r.json()) <= 2:
                    print ("White Light On!")
          if 3 <= len(r.json()) <= 5:
                    print ("Green Light On!")
          if 6 <= len(r.json()) <= 8:
                    print ("Blue Light On!")
          if 9 <= len(r.json()) <= 12:
                    print ("Yellow Light On!")
          if 13 <= len(r.json()) <= 16:
                    print ("Orange Light On!")
          if len(r.json()) > 16:
                    print ("Red Light On!")
                    

