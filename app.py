from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

JOBS = [
    {
        "title": "Software Engineer",
        "salary": "Rs. 1,000,000",
        "location": "Mountain View, CA",
        "description": "Work with a team of engineers to build software products for Google."
    },
    {
        "title": "Network Engineer",
        "salary": "Rs. 800,000",
        "location": "Menlo Park, CA",
        "description": "Lead a team of engineers to build network for Facebook"
    },
    {
        "title": "Data Scientist",
        "salary": "Rs. 1,200,000",
        "location": "San Francisco, CA",
        "description": "Analyze data to discover insights about Twitter users."

    },

    {
        "title": "Game Developer",
        "salary": "Rs. 1,100,000",
        "location": "Los Angeles, CA",
        "description": "Develop and design gameplay features for a major game studio."
    },
    {
        "title": "Unity Developer",
        "salary": "Rs. 950,000",
        "location": "San Diego, CA",
        "description": "Create immersive experiences using Unity for a leading VR company."
    },
    {
        "title": "Unreal Engine Developer",
        "salary": "Rs. 1,200,000",
        "location": "Austin, TX",
        "description": "Develop high-quality 3D environments and mechanics using Unreal Engine."
    },
    {
        "title": "Game Designer",
        "salary": "Rs. 1,000,000",
        "location": "Seattle, WA",
        "description": "Design and implement game mechanics and levels for an indie game studio."
    },
    {
        "title": "3D Artist",
        "salary": "Rs. 900,000",
        "location": "New York, NY",
        "description": "Create 3D models and textures for characters and environments in video games."
    },
    {
        "title": "Gameplay Programmer",
        "salary": "Rs. 1,050,000",
        "location": "San Francisco, CA",
        "description": "Implement gameplay systems and features for a top game development company."
    },
    {
        "title": "Technical Artist",
        "salary": "Rs. 1,000,000",
        "location": "Vancouver, BC",
        "description": "Bridge the gap between art and programming by creating tools and pipelines for artists."
    },
    {
        "title": "Game Producer",
        "salary": "Rs. 1,300,000",
        "location": "Toronto, ON",
        "description": "Oversee the development process and ensure timely delivery of game projects."
    },
    {
        "title": "Game Audio Designer",
        "salary": "Rs. 850,000",
        "location": "Chicago, IL",
        "description": "Design and implement audio assets for a wide range of video games."
    },
    {
        "title": "AI Programmer",
        "salary": "Rs. 1,150,000",
        "location": "Boston, MA",
        "description": "Develop AI systems and behaviors for non-playable characters and enemies."
    },
    {
        "title": "Game UX/UI Designer",
        "salary": "Rs. 950,000",
        "location": "Portland, OR",
        "description": "Create user interfaces and experiences for video games that are both functional and engaging."
    },
    {
        "title": "Game Systems Designer",
        "salary": "Rs. 1,000,000",
        "location": "Seattle, WA",
        "description": "Design and balance complex systems and mechanics within video games."
    },
    {
        "title": "Game Animator",
        "salary": "Rs. 900,000",
        "location": "Montreal, QC",
        "description": "Animate characters and objects in a game to bring them to life."
    },
    {
        "title": "Multiplayer Game Engineer",
        "salary": "Rs. 1,200,000",
        "location": "San Jose, CA",
        "description": "Develop and optimize multiplayer features and systems for online games."
    },
    {
        "title": "Virtual Reality Developer",
        "salary": "Rs. 1,100,000",
        "location": "Austin, TX",
        "description": "Build immersive VR experiences and applications for various platforms."
    },
    {
        "title": "Game Quality Assurance Tester",
        "salary": "Rs. 750,000",
        "location": "Los Angeles, CA",
        "description": "Test and identify bugs in games, ensuring they meet quality standards before release."
    },

    {
        "title": "Lead Game Developer",
        "salary": "Rs. 1,500,000",
        "location": "Los Angeles, CA",
        "description": "Lead a team of developers in creating and maintaining a major game title."
    },
    {
        "title": "Game Engine Programmer",
        "salary": "Rs. 1,200,000",
        "location": "Seattle, WA",
        "description": "Develop and maintain game engines and related tools for a top game studio."
    },
    {
        "title": "Game Level Designer",
        "salary": "Rs. 1,000,000",
        "location": "San Francisco, CA",
        "description": "Design and implement levels, environments, and challenges for video games."
    },
    {
        "title": "3D Environment Artist",
        "salary": "Rs. 950,000",
        "location": "Toronto, ON",
        "description": "Create detailed and visually appealing 3D environments for games."
    },
    {
        "title": "Character Animator",
        "salary": "Rs. 1,000,000",
        "location": "Vancouver, BC",
        "description": "Animate characters to bring them to life and ensure smooth movement and interactions."
    },
    {
        "title": "Graphics Programmer",
        "salary": "Rs. 1,200,000",
        "location": "New York, NY",
        "description": "Develop and optimize graphics and rendering techniques for video games."
    },
    {
        "title": "Game UI Programmer",
        "salary": "Rs. 950,000",
        "location": "San Diego, CA",
        "description": "Develop and implement user interfaces for video games, ensuring usability and aesthetic quality."
    },
    {
        "title": "Motion Capture Technician",
        "salary": "Rs. 850,000",
        "location": "Montreal, QC",
        "description": "Handle motion capture sessions and process data for use in game animations."
    },
    {
        "title": "Game Marketing Specialist",
        "salary": "Rs. 1,000,000",
        "location": "Chicago, IL",
        "description": "Develop and execute marketing strategies to promote video games and increase player engagement."
    },
    {
        "title": "Game Localization Specialist",
        "salary": "Rs. 900,000",
        "location": "Austin, TX",
        "description": "Translate and adapt game content for different languages and cultures."
    },
    {
        "title": "Augmented Reality Developer",
        "salary": "Rs. 1,100,000",
        "location": "San Jose, CA",
        "description": "Create AR applications and experiences using cutting-edge technology."
    },
    {
        "title": "Game Sound Designer",
        "salary": "Rs. 850,000",
        "location": "Seattle, WA",
        "description": "Design and implement sound effects and audio elements for video games."
    },
    {
        "title": "Technical Director",
        "salary": "Rs. 1,500,000",
        "location": "San Francisco, CA",
        "description": "Oversee technical aspects of game development, including programming, tools, and pipelines."
    },
    {
        "title": "Game Monetization Specialist",
        "salary": "Rs. 1,100,000",
        "location": "Los Angeles, CA",
        "description": "Develop and implement strategies for in-game purchases and other monetization methods."
    },
    {
        "title": "Gameplay Systems Engineer",
        "salary": "Rs. 1,200,000",
        "location": "Toronto, ON",
        "description": "Design and build complex gameplay systems and features for video games."
    },
    {
        "title": "Game Physics Programmer",
        "salary": "Rs. 1,150,000",
        "location": "Vancouver, BC",
        "description": "Implement and optimize physics systems to enhance realism and gameplay experience."
    },
    {
        "title": "Virtual World Designer",
        "salary": "Rs. 1,000,000",
        "location": "New York, NY",
        "description": "Create immersive and interactive virtual worlds for games and simulations."
    },
    {
        "title": "Game Narrative Designer",
        "salary": "Rs. 1,000,000",
        "location": "San Diego, CA",
        "description": "Develop and craft the story, dialogue, and narrative elements for video games."
    },
    {
        "title": "Game Production Assistant",
        "salary": "Rs. 750,000",
        "location": "Chicago, IL",
        "description": "Assist with various aspects of game production, including scheduling, coordination, and documentation."
    },
    {
        "title": "Game Community Manager",
        "salary": "Rs. 900,000",
        "location": "Austin, TX",
        "description": "Engage with the gaming community, manage forums, and handle feedback and inquiries."
    },
    {
        "title": "Game Systems Architect",
        "salary": "Rs. 1,300,000",
        "location": "Montreal, QC",
        "description": "Design and architect complex game systems and technologies for large-scale projects."
    },
    {
        "title": "Procedural Content Designer",
        "salary": "Rs. 1,050,000",
        "location": "San Jose, CA",
        "description": "Create algorithms and systems for generating procedural content in games."
    },
    {
        "title": "Game Quality Assurance Lead",
        "salary": "Rs. 950,000",
        "location": "Los Angeles, CA",
        "description": "Lead a QA team to test games, identify bugs, and ensure high quality before release."
    },
    {
        "title": "Game Storyboard Artist",
        "salary": "Rs. 850,000",
        "location": "San Francisco, CA",
        "description": "Create storyboards and visual plans for game narratives and cutscenes."
    },
    {
        "title": "Game Modder",
        "salary": "Rs. 800,000",
        "location": "Seattle, WA",
        "description": "Develop and release modifications for existing games, enhancing or changing gameplay."
    },
    {
        "title": "VR Interaction Designer",
        "salary": "Rs. 1,100,000",
        "location": "New York, NY",
        "description": "Design and implement interactive elements for virtual reality experiences."
    },
    {
        "title": "Game Development Instructor",
        "salary": "Rs. 1,000,000",
        "location": "Chicago, IL",
        "description": "Teach game development techniques and tools to students and aspiring developers."
    },
    {
        "title": "Game Cinematic Director",
        "salary": "Rs. 1,200,000",
        "location": "Vancouver, BC",
        "description": "Direct and oversee the creation of cinematic sequences and cutscenes for video games."
    },
    {
        "title": "Game User Researcher",
        "salary": "Rs. 950,000",
        "location": "San Diego, CA",
        "description": "Conduct research and gather data on player behavior to improve game design and features."
    },
    {
        "title": "Game Economy Designer",
        "salary": "Rs. 1,050,000",
        "location": "Toronto, ON",
        "description": "Design and balance in-game economies, including currency, rewards, and progression systems."
    },
    {
        "title": "Game Data Analyst",
        "salary": "Rs. 1,000,000",
        "location": "San Francisco, CA",
        "description": "Analyze game data to provide insights and recommendations for game design and improvement."
    },
    {
        "title": "Game AI Designer",
        "salary": "Rs. 1,100,000",
        "location": "Los Angeles, CA",
        "description": "Design and implement artificial intelligence systems for game characters and behaviors."
    },
    {
        "title": "Game Support Specialist",
        "salary": "Rs. 750,000",
        "location": "Seattle, WA",
        "description": "Provide technical support and assistance to players and address game-related issues."
    },
    {
        "title": "Game Build Engineer",
        "salary": "Rs. 1,050,000",
        "location": "Austin, TX",
        "description": "Manage and automate the process of building and deploying game software."
    },
    {
        "title": "Game VR/AR Tester",
        "salary": "Rs. 900,000",
        "location": "Montreal, QC",
        "description": "Test and evaluate virtual and augmented reality experiences for functionality and quality."
    }
]




@app.route("/careers")
def renderCareerPage():
    return render_template("careers.html", jobs=JOBS, companyName="Stealth")

@app.route("/")
def renderHome():
    return render_template("home.html", jobs=JOBS, companyName="Stealth")

@app.route("/hybridFarm")
def renderAboutHybridFarm():
    return render_template("hybridFarm.html", companyName="Stealth")

# @app.route("/api/jobs")
# def send_job():
#     return jsonify(JOBS)


if __name__ == "__main__":
    #print ("the name is The MAIN")
    #app.run(host='0.0.0.0',debug=True)  #for running within a private network
    app.run(host='0.0.0.0',debug=True)
