import streamlit as st
from PIL import Image

with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Yueyang Zhang, Ph.D.
##### *Resume* 
''')

image = Image.open('Photo.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Ph.D. graduate in Physiology, Cell and Developmental Biology with a specialization in aquatic toxicology. 
- Experience researcher with over 7 years of experience in aquatic toxicology with a passion for applying knowledge to create positive impacts on environment and economy.
- Strong track record in scholarly research.
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Yueyang Zhang</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#community-engagement-and-additional-activities">Community Engagement and Additional Activities</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#achievements">Achievements</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 0.57])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 0.8])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

def txt5(a, b):
    col1, col2 = st.columns([4, 0.57])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt6(a, b):
    col1, col2 = st.columns([4, 0.1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
#####################
st.markdown('''
## Education
''')

txt('**Doctor of Philosophy** (Biological Science), *University of Alberta*, Canada',
    '2015-2021')
st.markdown('''
- Physiology, cell and development biology with specialization in toxicology
- Research thesis entitled: `The Effects of Environmental Factors on the Toxicity of Nanomaterials in Fish`.
''')

txt('**Master of Biology** (Biological Science), *University of New Brunswick*, Canada',
    '2013-2015')
st.markdown('''
- Research thesis entitled: `The physiological and molecular responses of juvenile shortnose sturgeon to thermal stress`.
''')

txt('**Bachelors of Science** (Biological Science), *University of New Brunswick*, Canada',
    '2009-2013')
st.markdown('''
- GPA: 3.9
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt5('**Postdoctoral Fellow**, Biological Sciences, University of Alberta, Canada',
    '2021-Current')
st.markdown('''
- Mentor and supervise indigenous students in I-STEAM program, summer research students and master student. 
- Draft and apply for government organization grants and scholarships to secure funding for future research.
- Conduct research to assess the safety and effects of chemicals used in various industries on the aquatic environment.
''')

txt5('**Lecturer**, Biological Sciences, University of Alberta, Canada',
    'Winter 2022')
st.markdown('''
- Taught 70 undergraduate students on Biol 341: Ecotoxicology.
''')

txt5('**Lab instructor**, Biological Sciences, University of Alberta, Canada',
    '2015-2020')
st.markdown('''
- Taught over 300 undergraduate students on Biol 107 lab.
- Set up the lab and prepared materials for experiments.
- Supervised students in the lab.
- Organized tutorials and graded assignments and exams.
''')

txt5('**Teaching assistant**, Biological Sciences, University of Alberta, Canada',
    '2017-2019')
st.markdown('''
- Biol 341: Ecotoxicology.
- Organized tutorials and graded assignments and exams.
''')

txt5('**Teaching assistant**, Biological Sciences, University of New Brunswick, Canada',
    '2013-2015')
st.markdown('''
- Supervised students in the lab on Biol 1017 and Biol 3635.
- Organized tutorials and graded assignments and exams.
''')

txt5('**Research assistant**, Biological Sciences, University of New Brunswick, Canada',
    'Fall 2012')
st.markdown('''
- Conducted research (both laboratory and field-based) on the thermal tolerance and distribution of sturgeon species in the Saint John River in New Brunswick.
''')

#####################
st.markdown('''
## Community Engagement and Additional Activities
''')

txt('**Supervisor**, Biological Sciences, University of New Brunswick, Canada',
    '2018-2021')
st.markdown('''
- Mentored indigenous students in I-STEAM program.
- Mentored master student.
- Supervised summer research students in Undergraduate Research Initiative program.
- Supervised Biology 499 students in Undergraduate Research Initiative program
''')

txt('**Student co-chair**, 46th Canadian Ecotoxicity, Canada',
    '2018-2021')
st.markdown('''
- Monitored session “Alternative Approaches to Animal Testing for Ecotoxicity”
''')

txt('**Vice President in Biology Graduate Students’ Association**, University of Alberta, Canada',
    '2018-2019')
st.markdown('''
- Provided opportunity for graduate students to improve their academic skills by organizing workshops for candidacy exams and thesis writing.
- Provided a community and learning atmosphere (through meetings and forums) for biology graduate students.
- Organized recreational and fundraising events.
''')

txt('**Student councilor**, Biological Sciences, University of Alberta, Canada',
    '2017-2018')
st.markdown('''
- Monitored budget plan updates, course changes, scholarship applications and other affairs.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `Tableau`')
txt3('Web development', '`Flask`')
txt3('Model deployment', '`streamlit`')
txt6('GraphPad Prism', ' ')
txt6('Microsoft Office', ' ')
txt6('Nuclear Energy Worker', ' ')
txt6('Canadian Council on Animal Care certified animal user', ' ')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/yueyang-zhang-8448671bb/')
txt2('ORCID', 'https://orcid.org/my-orcid?orcid=0000-0001-9219-7637')

#####################
st.markdown('''
## Achievements
''')
txt6('Published 11 peer-reviewed articles in internationally accredited journals.', ' ')
txt6('Wrote a chapter for “Nanotoxicology” to review the nanotoxicology in the aquatic environment.', ' ')
txt6('Received two of the most prestigious scholarships in Canada: the Alberta Innovates-Graduate Student Scholarship and Mitacs Elevate, and over 15 other awards in chemistry, physics and biology.', ' ')
txt6('Presented at more than 20 national and international conferences and workshops', ' ')
