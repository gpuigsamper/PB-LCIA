import bw2data as bd

def get_biosphere_database():
    ERROR = "AESA methods work with ecoinvent biosphere flows only. Install base ecoinvent data."
    assert "ecoinvent-3.10.1-biosphere" in bd.databases, ERROR
    return list(bd.Database("ecoinvent-3.10.1-biosphere"))