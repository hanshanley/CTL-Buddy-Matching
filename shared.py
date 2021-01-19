class Student:
	def __init__(self, email, name, year, time_zone, meeting_freq, meeting_times, classes, major):
		self.email = email 
		self.name = name
		self.year = year
		self.time_zone = time_zone
		self.meeting_freq = meeting_freq
		self.meeting_times = meeting_times
		self.classes = classes
		self.major = major 

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__

time_zones = {
	'UTC-12:00 International Date Line West' : 12,
	'UTC-11:00 Coordinated Universal Time-11': 13,
	'UTC-10:00 Aleutian Islands T': 14,
	'UTC-09:00 Alaska': 15,
	'UTC-08:00 Pacific Time':16,
	'UTC-07:00 Mountain Time': 17,
	'UTC-06:00 Central Time': 18,
	'UTC-05:00 Eastern Time': 19,
	'UTC-04:00 Atlantic Time': 20,
	'UTC-03:00 Brasilia': 21,
	'UTC-02:00 Coordinated Universal Time-02':22,
	'UTC-01:00 Azores': 23,
	'UTC-00:00 London': 0,
	'UTC+01:00 Berlin, Paris': 1,
	'UTC+02:00 Jerusalem': 2,
	'UTC+03:00 Moscow': 3,
	'UTC+04:00 Abu Dhabi': 4,
	'UTC+05:00 Islamabad': 5,
	'UTC+06:00 Astana': 6,
	'UTC+07:00 Bangkok, Jakarta': 7,
	'UTC+08:00 Beijing, Hong Kong': 8,
	'UTC+09:00 Tokyo, Osaka, Seoul': 9,
	'UTC+10:00 Guam': 10,
	'UTC+11:00 Chokurdakh': 11,
	'UTC+12:00 Coordinated Universal Time+12': 12,
	'UTC+13:00 Coordinated Universal Time+13': 13,
	'UTC+14:00 Coordinated Universal Time+14': 14,
}

meeting_frequency = {
	'Daily': 1,
	'Weekly': 2,
	'Monthly': 3,
}

meeting_times = {
	'Morning 08:00-12:00': 10, 
	'Afternoon 12:00-16:00': 14,
	'Evening 16:00- 20:00': 18,
	'Night 20:00- 24:00': 22,
}

grad_majors_groups = {
	'Aeronautics and Astronautics' : 1,
	'Civil and Environmental Engineering' : 1 ,
	'Electrical Engineering': 1,
	'Mechanical Engineering': 1 ,
	'Bioengineering' : 2
	'Chemical Engineering':2 ,
	'Computational and Mathematical Engineering': 3, 
	'Computer Science' : 3, 
	'Design Impact':4,
	'Management Science and Engineering': 4,
	'Other Engineering': 5,
	'Anthropology': 1,
	'Classics': 1,
	'Communication': 1,
	'Economics':1,
	'History': 1,
	'International Policy':1,
	'Linguistics':1,
	'Philosophy': 1,
	'Political Science':1,
	'Psychology':1,
	'Public Policy':1,
	'Religious Studies':1,
	'Sociology':1,
	'English':2,
	'Modern Thought and Literature':2,
	'Comparative Literature':2,
	'Art History':3,
	'Art Practice':3,
	'Documentary Film and Video':3,
	'Theater and Performance Studies':3,
	'Master of Liberal Arts':3,
	'Music':3,
	'Mathematics':4,
	'Statistics':4,
	'Symbolic Systems':4,
	'East Asian Languages and Cultures':5,
	'East Asian Studies':5,
	'French and Italian':5,
	'French':5,
	'German Studies':5,
	'Iberian and Latin American Cultures':5,
	'Italian':5,
	'Latin American Studies':5,
	'Russian, East European, and Eurasian Studies':5,
	'Slavic Languages and Literature':5,
	'Applied Physics':6,
	'Chemistry':6,
	'Biology':6,
	'Biophysics':6,
	'Physics':6,
	'Other Humanities':7,
	'Other Sciences':8,
	'MD':1,
	'Biochemistry':2,
	'Biomedical informatics':2,
	'Cancer Biology':2,
	'Chemical and Systems Biology':2,
	'Developmental Biology':2,
	'Genetics':2,
	'Immunology':2,
	'Microbiology and Immunology':2,
	'Molecular and Cellular Physiology':2,
	'Neurosciences':2,
	'Stem Cell Biology and Regenerative Medicine':2,
	'Structural Biology':2,
	'Clinical Informatics Management':3,
	'Healthy Policy':3,
	'Human Genetics and Genetic Counseling':3,
	'Laboratory Animal Sciences':3,
	'Physician Assistant Studie':3,
	'Other Medicine/Biosciences':4,
	'Earth Systems Science':1,
	'Emmett Interdisciplinary Program in Environment and Resources':1,
	'Energy Resources Engineering':1,
	'Geological Sciences':1,
	'Geophysics':1,
	'Other SE3':1,
	'Law':1,
	'Business':1,
	'Curriculum Studies and Teacher Education (CTE)':1,
	'Developmental and Psychological Sciences (DAPS)':1,
	'International Comparative Education/International Education Policy Analysis':1,
	'Learning Design and Technology (LDT)':1,
	'Policy Organization and Leadership Studies (POLS)':1,
	'Stanford Teacher Education Program (STEP)':1,
	'Other Education':1,
	'Social Sciences, Humanities, and Interdisciplinary Policy Studies in Education':1,
}


### Tells types of grad major 
grad_major_types = {
	'Aeronautics and Astronautics' : 0,
	'Civil and Environmental Engineering' : 0 ,
	'Electrical Engineering': 0,
	'Mechanical Engineering': 0 ,
	'Bioengineering' : 0,
	'Chemical Engineering': 0 ,
	'Computational and Mathematical Engineering': 0 
	'Computer Science' : 0 
	'Design Impact': 0
	'Management Science and Engineering': 0
	'Other Engineering': 0 ,
	'Anthropology': 1,
	'Classics': 1,
	'Communication': 1,
	'Economics':1,
	'History': 1,
	'International Policy':1,
	'Linguistics':1,
	'Philosophy': 1,
	'Political Science':1,
	'Psychology':1,
	'Public Policy':1,
	'Religious Studies':1,
	'Sociology':1,
	'English':1,
	'Modern Thought and Literature':1,
	'Comparative Literature':1,
	'Art History':1,
	'Art Practice':1,
	'Documentary Film and Video':1,
	'Theater and Performance Studies':1,
	'Master of Liberal Arts':1,
	'Music':1,
	'Mathematics':1,
	'Statistics':1,
	'Symbolic Systems':1,
	'East Asian Languages and Cultures':1,
	'East Asian Studies':1,
	'French and Italian':1,
	'French':1,
	'German Studies':1,
	'Iberian and Latin American Cultures':1,
	'Italian':1,
	'Latin American Studies':1,
	'Russian, East European, and Eurasian Studies':1,
	'Slavic Languages and Literature':1,
	'Applied Physics':1,
	'Chemistry':1,
	'Biology':1,
	'Biophysics':1,
	'Physics':1,
	'Other Humanities':1,
	'Other Sciences':11,
	'MD':2,
	'Biochemistry':2,
	'Biomedical informatics':2,
	'Cancer Biology':2,
	'Chemical and Systems Biology':2,
	'Developmental Biology':2,
	'Genetics':2,
	'Immunology':2,
	'Microbiology and Immunology':2,
	'Molecular and Cellular Physiology':2,
	'Neurosciences':2,
	'Stem Cell Biology and Regenerative Medicine':2,
	'Structural Biology':2,
	'Clinical Informatics Management':2,
	'Healthy Policy':2
	'Human Genetics and Genetic Counseling':2,
	'Laboratory Animal Sciences':2,
	'Physician Assistant Studie':2,
	'Other Medicine/Biosciences':2,
	'Earth Systems Science':3,
	'Emmett Interdisciplinary Program in Environment and Resources':3,
	'Energy Resources Engineering':3,
	'Geological Sciences':3,
	'Geophysics':3,
	'Other SE3':3,
	'Law':4,
	'Business':5,
	'Curriculum Studies and Teacher Education (CTE)':6,
	'Developmental and Psychological Sciences (DAPS)':6,
	'International Comparative Education/International Education Policy Analysis':6,
	'Learning Design and Technology (LDT)':6,
	'Policy Organization and Leadership Studies (POLS)':6,
	'Stanford Teacher Education Program (STEP)':6,
	'Other Education':6,
	'Social Sciences, Humanities, and Interdisciplinary Policy Studies in Education':6,
}

type_of_work = {
	'Computational (i.e. Computer programming)': 0,
	'Experimental (i.e. Lab work)': 1,
	'Reading/Writing (i.e Literary Analysis)':2,
	'Test Preparation':3,
	'Other':4,

}
major_types = {
	'Undeclared/Undecided': 0,
	'Aeronautics and Astronautics': 1,
	'African and African American Studies': 3, 
	'African Studies': 3, 
	'American Studies': 3, 
	'Anthropology': 3, 
	'Applied and Engineering Physics' :1 , 
	'Archaeology': 3, 
	'Architectural Design': 3, 
	'Art History': 4, 
	'Art Practice': 4, 
	'Asian American Studies': 3, 
	'Atmosphere/Energy': 1, 
	'Bioengineering': 1,
	'Biology': 2,
	'Biomechanical Engineering': 1,
	'Biomedical Computation': 2, 
	'Chemical Engineering': 1,
	'Chemistry': 2, 
	'Chicana/o - Latina/o Studies': 3, 
	'Civil and Environmental Engineering': 1,
	'Classics': 4, 
	'Communication': 4, 
	'Community Health and Prevention Research': 2, 
	'Comparative Literature': 4, 
	'Comparative Studies in Race and Ethnicity': 4, 
	'Computer Science' : 1,
	'Democracy, Development, and the Rule of Law': 3, 
	'Earth Systems': 2, 
	'East Asian Studies': 3,
	'Economics': 3, 
	'Education': 3, 
	'Electrical Engineering' : 1,
	'Energy Resources Engineering': 1,
	'Engineering Physics' : 1, 
	'English': 4, 
	'Environmental Systems Engineering': 1,
	'Ethics in Society': 3, 
	'Feminist, Gender, and Sexuality Studies': 3,
	'Film and Media Studies': 4, 
	'French': 4, 
	'Geological Studies': 2, 
	'Geophysics': 2, 
	'German Studies': 3,
	'History': 3, 
	'Honors in the Arts': 4,
	'Human Biology': 2, 
	'Iberian and Latin American Cultures': 3, 
	'International Policy Studies': 3, 
	'International Relations': 3, 
	'International Security Studies': 3, 
	'Italian': 4, 
	'Jewish Studies': 3, 
	'Laboratory Animal Science': 2, 
	'Latin American Studies': 3, 
	'Linguistics': 4, 
	'Management Science and Engineering' : 1,
	'Materials Science and Engineering': 1,
	'Mathematical and Computational Science': 1,
	'Mathematics': 2, 
	'Mechanical Engineering': 1,
	'Modern Thought and Literature': 4,
	'Music': 4, 
	'Music, Science, and Technology': 2, 
	'Native American Studies': 3, 
	'Philosophy': 4, 
	'Philosophy and Religious Studies': 4,
	'Physics': 2, 
	'Political Science': 3, 
	'Product Design': 1,
	'Psychology': 2, 
	'Public Policy': 3, 
	'Religious Studies': 3, 
	'Science, Technology, and Society': 2, 
	'Slavic Languages and Literatures': 4, 
	'Sociology': 3, 
	'Spanish': 4, 
	'Statistics' : 2, 
	'Symbolic Systems': 1, 
	'Theater and Performance Studies': 4, 
	'Urban Studies': 3
}

year_type = {
	'Frosh': 1,
	'Sophomore': 2,
	'Junior': 3,
	'Senior': 4,
	'5th year+':5,
	'Co-term':6,
}

# strings for question prompts
q_full_name = 'Full Name'
q_year = 'Year'
q_email_address = 'Email Address'
q_time_zone = 'Time Zone (time zone where you will be located during Winter quarter)'
q_meeting_freq = 'How often do you wish to meet?'
q_meeting_times = 'Preferred Meeting Time(s)'
q_classes = 'Please select (up to four) courses for which you would want an accountability partner.'
q_major = 'Major'
q_program = 'Program'
q_research_type ='What type of research/work do you do?'
q_role = 'Role At Stanford'

class GradStudent:
	def __init__(self, email, name, role, time_zone, meeting_freq, meeting_times, work_type, major):
		self.email = email 
		self.name = name
		self.role = role
		self.time_zone = time_zone
		self.meeting_freq = meeting_freq
		self.meeting_times = meeting_times
		self.major = major 
		self.work_type = work_type

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__
