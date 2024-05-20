import geopandas as gpd
geopandas = gpd
import table
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))


d = geopandas.read_parquet("../intermediate/with_owner_analysis.pqt")


dimcolumns = list({
    "Total": True,
    "Likely onsite owner": d["LIKELY_OWNER_OCCUPIER"],
    "Likely not...": ~d["LIKELY_OWNER_OCCUPIER"]
}.items())

dimrows = list({
    "SFH": d["IS_SF"],
    "Duplex": d["IS_DUPLEX"],
    "Triplex": d["IS_TRIPLEX"],
    "4-8 unit": d["IS_FOUR_TO_EIGHT"],
    "9 or more units": (d["IS_FOUR_PLUS_APT"] & (~d["IS_FOUR_TO_EIGHT"]))
}.items())

result_table = table.cross_table(
    dimrows,
    dimcolumns,
    (lambda x, y: str((x&y).sum())),
    pretty=1
)

if __name__ == "__main__":
    print("HERE COMES A TABLE THAT HELPS GIVE INFO ABOUT RENT CONTROL EXEMPTIONS:\n\n")
    print(result_table)
