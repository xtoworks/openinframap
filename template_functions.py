from decimal import Decimal


def format_power(val):
    if val is None:
        return ""
    elif val >= 50e6:
        return "{:,.0f} MW".format(val / Decimal(1e6))
    elif val >= 1e6:
        return "{:.2f} MW".format(val / Decimal(1e6))
    else:
        return "{:.0f} kW".format(val / Decimal(1e3))


def osm_link(osm_id, geom_type):
    url = "https://www.openstreetmap.org/"
    if osm_id < 0:
        osm_id = -osm_id
        url += "relation"
    elif geom_type == "ST_Point":
        url += "node"
    else:
        url += "way"
    return url + "/" + str(osm_id)


THE_COUNTRY_NAMES = {"United States", "United Kingdom", "Netherlands", "Bahamas",
                     "Canary Islands", "British Virgin Islands", "Azores", "Cayman Islands"}


def country_name(name, cap=False):
    if name in THE_COUNTRY_NAMES:
        if cap:
            return "The " + name
        else:
            return "the " + name
    return name
