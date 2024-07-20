import json

def create_profile(name):
    with open('profiles.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
                        
                    
            data.append(
                {
                    'name': name
                }
            )
                
    with open('profiles.json', 'w+') as f:
        f.write(json.dumps(data, indent=4))