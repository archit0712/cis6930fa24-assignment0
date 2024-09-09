

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

# Test for thorn-separated file output
def test_parse_data():
    thorn_separated_output = parse_data(sample_data)
    assert thorn_separated_output == expected_output