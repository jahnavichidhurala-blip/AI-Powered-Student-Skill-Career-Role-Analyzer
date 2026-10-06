import streamlit as st
import random

st.set_page_config(
    page_title="AI-Powered Student Skill & Career Role Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Student Skill & Career Role Analyzer")

C = {
"Intermediate":{
"MPC":["Mathematics","Physics","Problem Solving"],
"BiPC":["Biology","Chemistry","Problem Solving"],
"MEC":["Mathematics","Economics","Accounting"],
"CEC":["Economics","Accounting","Communication"]},

"Diploma":{
"Computer Science Engineering":["Python","C Programming","Java","SQL","Data Structures","HTML","CSS"],
"Electronics & Communication Engineering":["C Programming","Digital Electronics","Electronic Circuits","Microcontrollers","Communication Systems"],
"Electrical & Electronics Engineering":["Electrical Circuits","Electrical Machines","Electronics","Power Systems","Control Systems"],
"Mechanical Engineering":["Engineering Mechanics","Thermodynamics","Manufacturing","CAD","Mechanical Design"],
"Civil Engineering":["Surveying","Construction","Structural Engineering","Engineering Drawing","Building Materials"],
"Automobile Engineering":["Automobile Basics","Engine Systems","Vehicle Maintenance","Automotive Electronics","CAD"],
"Data Science":["Python","SQL","Statistics","Data Analysis","Data Visualization"],
"Automation and Robotics Engineering":["Robotics","Automation","Python","C Programming","Arduino","Sensors","PLC"]},

"B.Tech / B.E":{
"Computer Science Engineering":["Python","Java","C Programming","Data Structures","SQL","HTML","CSS","JavaScript"],
"Information Technology":["Python","Java","SQL","HTML","CSS","Computer Networks","Cyber Security"],
"Artificial Intelligence & Machine Learning":["Python","Java","JavaScript","HTML","CSS","Data Structures","Mathematics","Statistics","Machine Learning","Data Analysis"],
"Data Science":["Python","SQL","Statistics","Data Analysis","Data Visualization"],
"Artificial Intelligence":["Python","Java","JavaScript","HTML","CSS","Data Structures","Mathematics","Machine Learning","Deep Learning","Data Analysis"],
"Cyber Security":["Python","Java","Data Structures","Computer Networks","Cyber Security","Linux","Cryptography"],
"Internet of Things":["Python","C Programming","Arduino","Sensors","Networking"],
"Robotics & Automation":["Robotics","Automation","Python","Arduino","Sensors","PLC","Control Systems"]},

"B.Sc":{
"B.Sc Computer Science":["Python","Java","C Programming","SQL","Data Structures"],
"B.Sc Data Science":["Python","Statistics","SQL","Data Analysis","Data Visualization"],
"B.Sc Mathematics":["Mathematics","Statistics","Problem Solving"],
"B.Sc Physics":["Physics","Mathematics","Problem Solving"],
"B.Sc Chemistry":["Chemistry","Mathematics","Problem Solving"],
"B.Sc Statistics":["Statistics","Mathematics","Data Analysis"],
"B.Sc Biotechnology":["Biology","Chemistry","Biotechnology"]},

"BCA":{
"BCA General":["Python","Java","SQL","HTML","CSS"],
"BCA Data Science":["Python","SQL","Statistics","Data Analysis"],
"BCA Artificial Intelligence & Machine Learning":["Python","Java","JavaScript","HTML","CSS","Data Structures","Mathematics","Machine Learning","Data Analysis"],
"BCA Cyber Security":["Python","Java","Data Structures","Computer Networks","Cyber Security","Linux"],
"BCA Full Stack Development":["HTML","CSS","JavaScript","Python","SQL"],
"BCA Data Analytics":["Python","SQL","Statistics","Data Analysis"]},

"MCA":{
"MCA General":["Python","Java","SQL","Data Structures"],
"MCA Artificial Intelligence":["Python","Java","JavaScript","HTML","CSS","Data Structures","Mathematics","Machine Learning","Deep Learning"],
"MCA Data Science":["Python","SQL","Statistics","Data Analysis"],
"MCA Cloud Computing":["Python","Java","Data Structures","Cloud Computing","Computer Networks","Linux"],
"MCA Cyber Security":["Python","Java","Data Structures","Cyber Security","Computer Networks","Linux"],
"MCA Software Development":["Python","Java","SQL","Data Structures"]},

"MBA":{
"MBA Finance":["Accounting","Financial Analysis","Excel","Business Analytics"],
"MBA Marketing":["Marketing","Communication","Digital Marketing","Business Analytics"],
"MBA Human Resources":["Communication","Leadership","Human Resources","Management"],
"MBA Business Analytics":["Excel","Statistics","Data Analysis","Business Analytics"],
"MBA Operations Management":["Operations","Management","Business Analytics","Excel"],
"MBA Entrepreneurship":["Business Planning","Leadership","Marketing","Communication"]},

"Other":{"General":["Communication","Problem Solving","Computer Basics"]}
}

Q = {
"Python":[("Function keyword?","def"),("Output function?","print"),("Boolean type?","bool")],
"Java":[("Class keyword?","class"),("Starting method?","main"),("Object keyword?","new")],
"C Programming":[("Statement ending symbol?",";"),("Output function?","printf"),("Printf header?","stdio.h")],
"SQL":[("Get data command?","select"),("Add row command?","insert"),("Remove table command?","drop")],
"Data Structures":[("LIFO structure?","stack"),("FIFO structure?","queue"),("Nodes and links?","linked list")],
"HTML":[("Paragraph tag?","p"),("Link tag?","a"),("Largest heading?","h1")],
"CSS":[("Text color property?","color"),("Background property?","background-color"),("CSS is used for?","styling")],
"JavaScript":[("Variable keyword?","let"),("Message function?","alert"),("JS adds?","interactivity")],
"Mathematics":[("12 × 5?","60"),("√81?","9"),("25% of 100?","25")],
"Physics":[("Force unit?","newton"),("Earth pulling force?","gravity"),("Energy unit?","joule")],
"Problem Solving":[("2,4,6,8 next?","10"),("5 + 5?","10"),("10 - 4?","6")],
"Biology":[("Blood pumping organ?","heart"),("Basic life unit?","cell"),("Breathing organs?","lungs")],
"Chemistry":[("Oxygen symbol?","o"),("H2O is?","water"),("Pure water pH?","7")],
"Economics":[("Basic economic problem?","scarcity"),("Study of production?","economics"),("People buying goods?","consumers")],
"Accounting":[("Accounting equation?","assets=liabilities+capital"),("Money received?","revenue"),("Money spent?","expense")],
"Communication":[("Communication exchanges?","information"),("Understanding speech?","listening"),("Information exchange?","communication")],
"Digital Electronics":[("0 and 1 system?","binary"),("NOT gate inputs?","1"),("All inputs 1 gate?","and")],
"Electronic Circuits":[("Current resisting component?","resistor"),("Charge storing component?","capacitor"),("Amplifying component?","transistor")],
"Microcontrollers":[("Computer on a chip?","microcontroller"),("Programmable controller?","microcontroller"),("Arduino controller?","avr")],
"Communication Systems":[("Information carrier?","signal"),("Electrical to sound?","speaker"),("Wireless waves?","radio")],
"Electrical Circuits":[("Current unit?","ampere"),("Resistance unit?","ohm"),("Voltage-current law?","ohm's law")],
"Electrical Machines":[("Electrical to mechanical?","motor"),("Mechanical to electrical?","generator"),("Transformer uses?","ac")],
"Electronics":[("One-way current device?","diode"),("Charge storing device?","capacitor"),("Amplifying device?","transistor")],
"Power Systems":[("Long-distance power transfer?","transmission lines"),("Power unit?","watt"),("AC voltage changer?","transformer")],
"Control Systems":[("System with feedback?","closed loop"),("Desired minus actual?","error"),("No feedback?","open loop")],
"Engineering Mechanics":[("Force unit?","newton"),("Turning effect?","moment"),("Motion resistance?","inertia")],
"Thermodynamics":[("Temperature unit?","kelvin"),("Temperature energy transfer?","heat"),("First law conservation?","energy")],
"Manufacturing":[("Material removal?","machining"),("Metal joining?","welding"),("Mold process?","casting")],
"CAD":[("CAD full form?","computer aided design"),("CAD creates?","drawings"),("Solid model?","3d model")],
"Mechanical Design":[("Bearing reduces?","friction"),("Pulling force?","tension"),("Pushing force?","compression")],
"Surveying":[("Surveying measures?","land"),("Angle instrument?","theodolite"),("Distance tool?","tape")],
"Construction":[("Concrete needs?","water"),("Reinforcement?","steel"),("Foundation transfers load to?","ground")],
"Structural Engineering":[("Beam resists?","bending"),("Column carries?","compression"),("Concrete reinforcement?","steel")],
"Engineering Drawing":[("Front side view?","front view"),("Circle tool?","compass"),("Drawing measurements?","dimensions")],
"Building Materials":[("Structural material?","concrete"),("Brick material?","clay"),("Concrete reinforcement?","steel")],
"Automobile Basics":[("Stopping system?","braking system"),("Power transfer system?","transmission"),("Direction system?","steering")],
"Engine Systems":[("Fuel to mechanical energy?","internal combustion engine"),("Fuel supply?","fuel system"),("Heat removal?","cooling system")],
"Vehicle Maintenance":[("Engine oil provides?","lubrication"),("Braking safety check?","brakes"),("Electrical storage?","battery")],
"Automotive Electronics":[("Vehicle control unit?","ecu"),("Engine temperature sensor?","temperature sensor"),("Vehicle storage?","battery")],
"Robotics":[("Robot performs?","tasks"),("Movement component?","actuator"),("Environment detector?","sensor")],
"Automation":[("Automation reduces human?","intervention"),("Process controller?","control system"),("Automation improves?","productivity")],
"Arduino":[("Arduino is a?","microcontroller board"),("Arduino language?","c++"),("Startup function?","setup")],
"Sensors":[("Sensor detects?","physical quantity"),("Temperature sensor?","temperature sensor"),("Distance sensor?","ultrasonic sensor")],
"PLC":[("PLC full form?","programmable logic controller"),("PLC used for?","industrial automation"),("PLC diagram?","ladder logic")],
"Statistics":[("Average?","mean"),("Middle value?","median"),("Most frequent?","mode")],
"Data Analysis":[("Examining data?","data analysis"),("Python data library?","pandas"),("Organized data?","dataset")],
"Data Visualization":[("Category chart?","bar chart"),("Trend chart?","line chart"),("Whole-parts chart?","pie chart")],
"Machine Learning":[("ML learns from?","data"),("Labeled learning?","supervised learning"),("Unlabeled learning?","unsupervised learning")],
"Deep Learning":[("Deep learning uses?","neural networks"),("Deep learning is part of?","machine learning"),("Image network?","cnn")],
"Computer Networks":[("LAN full form?","local area network"),("Network connector?","router"),("Web protocol?","http")],
"Cyber Security":[("Protects from?","threats"),("Secret protection word?","password"),("Malware detector?","antivirus")],
"Linux":[("Linux is an?","operating system"),("List files?","ls"),("Change directory?","cd")],
"Cryptography":[("Data protection?","encryption"),("Readable data conversion?","encryption"),("Unlocking item?","key")],
"Networking":[("Local network device?","switch"),("IP full form?","internet protocol"),("Network identifier?","ip address")],
"Cloud Computing":[("Cloud uses?","internet"),("Virtual machine service?","iaas"),("Cloud data stored on?","servers")],
"Excel":[("Spreadsheet software?","excel"),("Row-column intersection?","cell"),("Formula starts?","=")],
"Financial Analysis":[("Profit?","revenue-expenses"),("Financial position statement?","balance sheet"),("Analysis evaluates?","performance")],
"Business Analytics":[("Data supports?","decisions"),("Business + data field?","business analytics"),("Finding patterns?","analysis")],
"Marketing":[("Marketing promotes?","products"),("Online marketing?","digital marketing"),("Buyers?","customers")],
"Digital Marketing":[("Digital marketing uses?","internet"),("SEO full form?","search engine optimization"),("Marketing through?","email")],
"Leadership":[("Leadership guides?","people"),("Important skill?","listening"),("Leaders make?","decisions")],
"Human Resources":[("HR manages?","employees"),("Recruitment finds?","employees"),("HR full form?","human resources")],
"Management":[("Management controls?","resources"),("Manager coordinates?","people"),("Management achieves?","goals")],
"Operations":[("Operations produces?","goods and services"),("Operations improves?","efficiency"),("Stored goods?","inventory")],
"Business Planning":[("Business plan describes?","business"),("Financial plan includes?","projections"),("Planning sets?","goals")],
"Biotechnology":[("Biotechnology uses?","living organisms"),("Biology + ?","technology"),("DNA found in?","cells")],
"Computer Basics":[("CPU full form?","central processing unit"),("Text input device?","keyboard"),("Display device?","monitor")]
}

CAREER = {
"Python":["Python Developer","AI Engineer","Data Analyst"],
"Java":["Java Developer","Software Developer"],
"SQL":["Database Developer","Data Analyst"],
"HTML":["Web Developer"],"CSS":["Frontend Developer"],
"JavaScript":["Frontend Developer","Full Stack Developer"],
"Data Structures":["Software Engineer"],
"Machine Learning":["ML Engineer","AI Engineer"],
"Cyber Security":["Cyber Security Analyst"],
"Computer Networks":["Network Engineer"],
"Robotics":["Robotics Engineer"],
"Automation":["Automation Engineer"],
"PLC":["PLC Programmer"],"CAD":["CAD Designer"],
"Statistics":["Data Analyst"],"Accounting":["Accountant"],
"Communication":["HR Executive","Marketing Executive"],
"Leadership":["Team Leader","Manager"],
"Business Analytics":["Business Analyst"]
}

def level(x):
    return "Expert" if x>=90 else "Advanced" if x>=75 else "Intermediate" if x>=60 else "Basic" if x>=40 else "Beginner"

st.header("👤 Student Details")
name = st.text_input("Student Name")

st.header("📚 Education")
edu = st.selectbox("Education", list(C))
course = st.selectbox("Course / Branch / Specialization", list(C[edu]))

st.header("💡 Skills")
skills = st.multiselect("Select Skills", C[edu][course])

if st.button("🚀 Start Skill Assessment"):
    if not name or not skills:
        st.warning("Enter name and select skills.")
    else:
        st.session_state.q = {s: random.sample(Q[s],3) for s in skills}
        st.session_state.skills = skills
        st.session_state.allskills = C[edu][course]
        st.session_state.started = True
        st.session_state.result = None
        st.rerun()

if st.session_state.get("started"):
    st.header("📝 Skill Assessment")

    with st.form("test"):
        A = {}
        n = 0
        for s in st.session_state.skills:
            st.subheader(f"🔹 {s}")
            for q,a in st.session_state.q[s]:
                n += 1
                A[n] = st.text_input(f"Q{n}. {q}", key=f"a{n}")
        done = st.form_submit_button("📊 Calculate Score")

    if done:
        R = {}
        n = 0
        for s in st.session_state.skills:
            score = 0
            for q,a in st.session_state.q[s]:
                n += 1
                score += A[n].strip().lower() == a.lower()
            R[s] = round(score/3*100,2)
        st.session_state.result = R
        st.rerun()

if st.session_state.get("result") is not None:
    R = st.session_state.result

    st.header("📊 Assessment Result")
    for s,p in R.items():
        st.write(f"**{s}: {p}% — {level(p)}**")
        st.progress(int(p))

    st.header("⚠️ Missing / Weak Skills")
    missing = [
        s if s not in R else f"{s} — {R[s]}%"
        for s in st.session_state.allskills
        if s not in R or R[s] < 60
    ]

    if missing:
        for s in missing:
            st.warning(s)
    else:
        st.success("🎉 No missing or weak skills!")

    st.header("🚀 Recommended Career Roles")
    careers = []
    for s,p in R.items():
        if p >= 60:
            careers += CAREER.get(s,[])

    for c in list(dict.fromkeys(careers))[:5]:
        st.success(f"💼 {c}")