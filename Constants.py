# Constants
GEOFILE = "lang_aurin.json"

AURIN_INCOME = "income_aurin.json"

AURIN_LANGUAGE = "lang_aurin.json"

AURIN_HEALTH = "medi_aurin.json"

LARGE_TWITTER = "twitter-melb.json"

EMPLOYMENT = ["employment","job", "occupation", "income", "pay"]

HEALTH = ["health", "hospital","sick","unwell","doctor", "medicine", "drug"]

TOPICS = [['diversity'], EMPLOYMENT, HEALTH]

READ_LIMIT = 10000

END_OF_LINE_START = -2 #the Index of where a line should end if it is first line of the large twitter file

END_OF_LINE_BODY = -3 #the Index of where a line should end if it locates within middle of the large twitter file

END_OF_LINE_END = -4 #the Index of where a line should end if it is the last line of the the large twitter file
