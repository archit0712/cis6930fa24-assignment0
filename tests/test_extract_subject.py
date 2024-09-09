from main import parse_data
import json

f = open("result.json", "r")

sample_data = json.load(f)

expected_output = [
    "HANSEL QUIROZþKidnappings and Missing Personsþlosangeles",
    "FELIPE DE JESUS QUIROZ-JIMENEZþParental Kidnappingþlosangeles",
    "CINDY RODRIGUEZ SINGHþViolent Crimes - Murdersþdallas",
    "STEPHANIE MARIE GANT-BRADY - BALTIMORE, MARYLANDþViCAP Missing Personsþ",
    "JESUS DE LA CRUZ - LYNN, MASSACHUSETTSþViCAP Missing Personsþ",
    "BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork",
    "AARON PAUL VICTORYþAdditional Violent Crimesþoklahomacity",
    "IDA DEAN (RICHARDSON) ANDERSON - ANN ARBOR, MICHIGANþViCAP Missing Personsþ",
    "HUYEN TRANG TEMPLE - ARSONþSeeking Informationþhouston",
    "BRYAN MATTHEW MCGEHRIN - TANEYTOWN, MARYLANDþViCAP Missing Personsþ",
    "JOHN DOE - WATERLOO TOWNSHIP, MICHIGANþViCAP Unidentified Personsþ",
    "MITCHELL TODD HEIN - INDIO, CALIFORNIAþViCAP Missing Personsþ",
    "ELSIE ELDORA LUSCIERþKidnappings and Missing Persons,Indian Countryþseattle",
    "ATRAYA BERARDI - ROCKLEDGE, FLORIDAþþ",
    "KOA KAI BERNSTEINþKidnappings and Missing Personsþhonolulu",
    "DHULFIQAR KAREEM MSEERþSeeking Informationþportland",
    "FREDERICK ARIASþWhite-Collar Crimeþphoenix",
    "RODOLFO MANTILLAþCriminal Enterprise Investigationsþmiami",
    "RANDY STEWART DORAN - NEW ORLEANS, LOUISIANAþViCAP Missing Personsþ",
    "DARASY S. CHHIMþCriminal Enterprise Investigationsþboston"
]

def extract_subject(parsed_data):
    """
    Extract only subjects from the thorn-separated values.
    """
    subjects = []
    for row in parsed_data:
        title = row.split('þ')[1]  # Split by 'þ' and take the first part (title)
        subjects.append(title)
    return subjects
# Test extracting subjects from FBI API data
def test_extract_subject():
    parsed_data = parse_data(sample_data)
    result_subjects = extract_subject(parsed_data)
    expected_subjects = extract_subject(expected_output)
    
    assert expected_subjects == result_subjects
# Test fetching data from a file and ensuring thorn-separated values are correct