from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 10
popular = {
    "1": {
        "id":"1",
        "name":"Jett",
        "agent_tutorial":"https://www.youtube.com/watch?v=oQvTydlhNu0",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltceaa6cf20d328bd5/5eb7cdc1b1f2e27c950d2aaa/V_AGENTS_587x900_Jett.png",
        "agent_trailer":"https://www.youtube.com/watch?v=-cPLXswVsvc",
        "description":"Representing her home country of South Korea, Jett's agile and evasive fighting style lets her take risks no one else can. She runs circles around every skirmish, cutting enemies before they even know what hit them.",
        "year_added":"2020",
        "abilities":["Cloudburst","Updraft","Tailwind","BladeStorm"],
        "agent_type": "Duelist"
    },
    "2": {
        "id":"2",
        "name":"Phoenix",
        "agent_tutorial":"https://www.youtube.com/watch?v=ltcs81Kz5-g",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf0200e1821b5b39f/5eb7cdc144bf8261a04d87f9/V_AGENTS_587x900_Phx.png",
        "agent_trailer":"https://www.youtube.com/watch?v=ttJMFW2wUQM",
        "description":"Hailing from the U.K., Phoenix's star power shines through in his fighting style, igniting the battlefield with flash and flare. Whether he's got backup or not, he'll rush into a fight on his own terms.",
        "year_added":"2020",
        "abilities":["Blaze","Curveball","Hot hands","Run it back"],
        "agent_type": "Duelist"
    },
    "3": {
        "id":"3",
        "name":"Neon",
        "agent_tutorial":"https://www.youtube.com/watch?v=Mu-s0UtFA64",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png",
        "agent_trailer":"https://www.youtube.com/watch?v=dtx8CgjRmqE",
        "description":"Filipino Agent Neon surges forward at shocking speeds, discharging bursts of bioelectric radiance as fast as her body generates it. She races ahead to catch enemies off guard, then strikes them down quicker than lightning.",
        "year_added":"2022",
        "abilities":["Fast lane","Relay bolt","High Gear","Overdrive"],
        "agent_type": "Duelist"
    }
}

data = {
    "1": {
        "id":"1",
        "name":"Jett",
        "agent_tutorial":"https://www.youtube.com/watch?v=oQvTydlhNu0",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltceaa6cf20d328bd5/5eb7cdc1b1f2e27c950d2aaa/V_AGENTS_587x900_Jett.png",
        "agent_trailer":"https://www.youtube.com/watch?v=-cPLXswVsvc",
        "description":"Representing her home country of South Korea, Jett's agile and evasive fighting style lets her take risks no one else can. She runs circles around every skirmish, cutting enemies before they even know what hit them.",
        "year_added":"2020",
        "abilities":["Cloudburst","Updraft","Tailwind","BladeStorm"],
        "agent_type": "Duelist"
    },
    "2": {
        "id":"2",
        "name":"Phoenix",
        "agent_tutorial":"https://www.youtube.com/watch?v=ltcs81Kz5-g",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf0200e1821b5b39f/5eb7cdc144bf8261a04d87f9/V_AGENTS_587x900_Phx.png",
        "agent_trailer":"https://www.youtube.com/watch?v=ttJMFW2wUQM",
        "description":"Hailing from the U.K., Phoenix's star power shines through in his fighting style, igniting the battlefield with flash and flare. Whether he's got backup or not, he'll rush into a fight on his own terms.",
        "year_added":"2020",
        "abilities":["Blaze","Curveball","Hot hands","Run it back"],
        "agent_type": "Duelist"
    },
    "3": {
        "id":"3",
        "name":"Neon",
        "agent_tutorial":"https://www.youtube.com/watch?v=Mu-s0UtFA64",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png",
        "agent_trailer":"https://www.youtube.com/watch?v=dtx8CgjRmqE",
        "description":"Filipino Agent Neon surges forward at shocking speeds, discharging bursts of bioelectric radiance as fast as her body generates it. She races ahead to catch enemies off guard, then strikes them down quicker than lightning.",
        "year_added":"2022",
        "abilities":["Fast lane","Relay bolt","High Gear","Overdrive"],
        "agent_type": "Duelist"
    },
    "4": {
        "id":"4",
        "name":"Raze",
        "agent_tutorial":"https://www.youtube.com/watch?v=YaSALibswVE",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6fef56a8182d0a81/5ebf2c2798f79d6925dbd6b4/V_AGENTS_587x900_ALL_Raze_2.png",
        "agent_trailer":"https://www.youtube.com/watch?v=ZGvz7jTVbc8",
        "description":"Raze explodes out of Brazil with her big personality and big guns. With her blunt-force-trauma playstyle, she excels at flushing entrenched enemies and clearing tight spaces with a generous dose of “boom.”",
        "year_added":"2020",
        "abilities":["Boombot","Blast pack","Paintshells","Showstopper"],
        "agent_type": "Duelist"
    },
    "5": {
        "id":"5",
        "name":"Reyna",
        "agent_tutorial":"https://www.youtube.com/watch?v=Ynac3J_VRC8",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6577b1f58530e6b2/5eb7cdc121a5027d77420208/V_AGENTS_587x900_Reyna.png",
        "agent_trailer":"https://www.youtube.com/watch?v=IzsQNYrq9AM",
        "description":"Forged in the heart of Mexico, Reyna dominates single combat, popping off with each kill she scores. Her capability is only limited by her raw skill, making her highly dependent on performance.",
        "year_added":"2020",
        "abilities":["Leer","Devour","Dismiss","Empress"],
        "agent_type": "Duelist"
    },
    "6": {
        "id":"6",
        "name":"Yoru",
        "agent_tutorial":"https://www.youtube.com/watch?v=yU7mQdAdXzY",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd4080f8efb365751/5ff5660bb47cdf7fc7d6c3dc/V_AGENTS_587x900_yoru.png",
        "agent_trailer":"https://www.youtube.com/watch?v=GdOEQv-zQVw",
        "description":"Japanese native, Yoru, rips holes straight through reality to infiltrate enemy lines unseen. Using deception and aggression in equal measure, he gets the drop on each target before they know where to look.",
        "year_added":"2021",
        "abilities":["Fakeout","Blindside","Gatecrash","Dimensional Drift"],
        "agent_type": "Duelist"
    },
    "7": {
        "id":"7",
        "name":"Astra",
        "agent_tutorial":"https://www.youtube.com/watch?v=kueP3oPloFk",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5599d0d810824279/6036ca30ce4a0d12c3ec1dfa/V_AGENTS_587x900_Astra.png",
        "agent_trailer":"https://www.youtube.com/watch?v=-ylVnuPWlJM",
        "description":"Ghanaian Agent Astra harnesses the energies of the cosmos to reshape battlefields to her whim. With full command of her astral form and a talent for deep strategic foresight, she's always eons ahead of her enemy's next move.",
        "year_added":"2021",
        "abilities":["Gravity well","Nove pulse","Nebula","Astral form"],
        "agent_type": "Controller"
    },
    "8": {
        "id":"8",
        "name":"Brimstone",
        "agent_tutorial":"https://www.youtube.com/watch?v=7eWVlupZZE8",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt26fcf1b5752514ee/5eb7cdbfc1dc88298d5d3799/V_AGENTS_587x900_Brimstone.png",
        "agent_trailer":"https://www.youtube.com/watch?v=7yHnJ_oNxTI",
        "description":"Joining from the USA, Brimstone's orbital arsenal ensures his squad always has the advantage. His ability to deliver utility precisely and from a distance make him an unmatched boots-on-the-ground commander.",
        "year_added":"2020",
        "abilities":["Stim beacon","Incendiary","Sky smoke","Orbital strike"],
        "agent_type": "Controller"
    },
    "9": {
        "id":"9",
        "name":"Omen",
        "agent_tutorial":"https://www.youtube.com/watch?v=wGsF5ZDkd5I",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4e5af408cc7a87b5/5eb7cdc17bedc8627eff8deb/V_AGENTS_587x900_Omen.png",
        "agent_trailer":"https://www.youtube.com/watch?v=_jJdWy6bDj4",
        "description":"A phantom of a memory, Omen hunts in the shadows. He renders enemies blind, teleports across the field, then lets paranoia take hold as his foe scrambles to learn where he might strike next.",
        "year_added":"2020",
        "abilities":["Shrouded step","Paranoia","Dark covers","From the shadows"],
        "agent_type": "Controller"
    },
    "10": {
        "id":"10",
        "name":"Breach",
        "agent_tutorial":"https://www.youtube.com/watch?v=UwhN6svtlHE&t=242s",
        "agent_image":"https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt100d13bfa8286a3d/5eb7cdc11ea0c32e33b95fa2/V_AGENTS_587x900_Breach.png",
        "agent_trailer":"https://www.youtube.com/watch?v=Rux0HjzKQbw",
        "description":"Breach, the bionic Swede, fires powerful, targeted kinetic blasts to aggressively clear a path through enemy ground. The damage and disruption he inflicts ensures no fight is ever fair.",
        "year_added":"2020",
        "abilities":["Aftershock","Flashpoint","Fault line","Rolling thunder"],
        "agent_type": "Controller"
    },
}

# ROUTES



@app.route('/')
def hello_world():
   global popular;
   return render_template('welcome.html', popular=popular)


@app.route('/agent/<name>')
def hello_name(name=None):
    global data
    single_data = data[name]
    return render_template('hello_agent.html', single_data=single_data)


# AJAX FUNCTIONS

# ajax for people.js
@app.route('/search/<text>')
def search_name(text=None):
    global data;
    lists = []

    for a in data.values():
        if text.lower() in a['name'].lower() or text.lower() in a['agent_type'].lower() or text.lower() in a['year_added']:
            lists.append({"id": a['id'], "name": a['name'], "agent_type": a['agent_type'], "year_added": a['year_added'], "agent_image": a['agent_image'], "agent_type": a['agent_type']})

    length_list = len(lists)

    return render_template('search.html',lists=lists, text=text, length_list=length_list)

@app.route('/add')
def add():
    global data;
    return render_template('add.html')


@app.route('/save_entry', methods=['GET', 'POST'])
def save_entry():
    global data
    global current_id

    json_data = request.get_json()
    name = json_data["name"]
    tut = json_data["agent_tutorial"]
    trail = json_data["agent_trailer"]
    images = json_data["agent_image"]
    desc = json_data["description"]
    abl = json_data["abilities"]
    yr = json_data["year_added"]
    typ = json_data["agent_type"]


    # add new entry to array with
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = str(current_id)
    new_name_entry =  {
        "id": new_id,
        "name": name,
        "agent_tutorial":tut,
        "agent_image":trail,
        "agent_trailer":images,
        "description":desc,
        "year_added":yr,
        "abilities":abl,
        "agent_type": typ

    }
    data[new_id]=new_name_entry



    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data=data, alert_id=new_id)






@app.route('/edit/<name>')
def edit_data(name=None):
    global data
    single_data = data[name]
    return render_template('edit.html', single_data=single_data, curr_id=name)



@app.route('/edit/edit_entry', methods=['GET', 'POST'])
def edit_entry():
    global data


    json_data = request.get_json()
    id_rn = json_data["id_rn"]
    name = json_data["name"]
    tut = json_data["agent_tutorial"]
    trail = json_data["agent_trailer"]
    images = json_data["agent_image"]
    desc = json_data["description"]
    abl = json_data["abilities"]
    yr = json_data["year_added"]
    typ = json_data["agent_type"]

    new_name_entry =  {
        "id": id_rn,
        "name": name,
        "agent_tutorial":tut,
        "agent_image":trail,
        "agent_trailer":images,
        "description":desc,
        "year_added":yr,
        "abilities":abl,
        "agent_type": typ

    }
    data[id_rn]=new_name_entry
    return jsonify(data=data, curr_id=id_rn)

if __name__ == '__main__':
   app.run(debug = True)
