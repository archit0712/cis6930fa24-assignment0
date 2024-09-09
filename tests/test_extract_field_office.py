from main import parse_data
import json

#  Open the file in read mode
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

def extract_field_office(parsed_data):
    """
    Extract only field_offices from the thorn-separated values.
    """
    field_offices = []
    for row in parsed_data:
        title = row.split('þ')[2]  # Split by 'þ' and take the first part (title)
        field_offices.append(title)
    return field_offices
# Test extracting field_offices from FBI API data
def test_extract_field_office():
    parsed_data = parse_data(sample_data)
    result_field_offices = extract_field_office(parsed_data)
    expected_field_offices = extract_field_office(expected_output)
    
    assert expected_field_offices == result_field_offices
# Test fetching data from a file and ensuring thorn-separated values are correct