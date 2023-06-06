import folium
from dataclasses import dataclass
from geopy import distance



@dataclass
class Marker:
    name: str
    descriptions: str
    lat: float  # latitude
    long: float  # longitude


@dataclass
class Circut:
    name: str
    lat: float
    long: float
    radius: int


markers = [
    dinamo := Marker("dinamo","dinamo", 54.988144, 73.360309),
    sobor := Marker("sobor","sobor", 54.990163, 73.366649),
    school_66 := Marker("school_66","school_66", 54.998086, 73.358870),
    omgau := Marker("omgau","omgau", 54.998086, 73.358870),
    metalist := Marker("metalist","metalist", 55.005108, 73.360576),
    liza_park := Marker("liza_park", "liza_park", 54.972215, 73.419350),
    pobedy_park := Marker("pobedy_park", "pobedy_park", 54.961690, 73.359938),
    mega := Marker("mega", "mega", 54.971659, 73.285662),
    autovokzal := Marker("autovokzal","autovokzal", 54.998618, 73.281255),
    telecentr := Marker("telecentr", "telecentr", 55.022123, 73.307333),
    crystal := Marker("crystal","crystal", 55.028522, 73.284507),
    school_61 := Marker("school_61","school_61", 55.037582, 73.294586),
    himik := Marker("himik","himik", 55.042303, 73.295035),
    vesna := Marker("vesna","vesna", 55.029315, 73.249763),
    lenta_amur := Marker("lenta_amur","lenta_amur", 55.035971, 73.416491),
    dk_kolos := Marker("dk_kolos","dk_kolos", 55.065669, 73.417727),
    poselok_omskiy := Marker("poselok_omskiy","poselok_omskiy", 55.101813, 73.349626),
    poselok_podgorodka := Marker("poselok_podgorodka","poselok_podgorodka", 55.143093, 73.548335),
    poselok_hvoiny := Marker("poselok_hvoiny","poselok_hvoiny", 55.110584, 73.580322),
    poselok_rostovka := Marker("poselok_rostovka","poselok_rostovka", 55.020270, 73.575121),
    jd_vokzal := Marker("jd_vokzal", "jd_vokzal", 54.939560, 73.385721),
    school_20 := Marker("school_20", "school_20", 54.907496, 73.357351),
    agroprom := Marker("agroprom", "agroprom", 54.911893, 73.301592),
    poselok_morozovka := Marker("poselok_morozovka", "poselok_morozovka", 54.924548, 73.549382),
    poselok_rakitinka := Marker("poselok_rakitinka", "poselok_rakitinka", 54.898357, 73.520180),
    putevaya := Marker("putevaya", "putevaya", 54.917225, 73.435557),
    ledoviy_dvorec := Marker("ledoviy_dvorec", "ledoviy_dvorec", 54.921137, 73.457235),
    gasheka := Marker("gasheka", "gasheka", 54.908537, 73.444933),
    metro := Marker("metro", "metro", 54.896516, 73.429477)
]

circuts = [
    zone_0 := Circut("zone0", 54.991372, 73.363910, radius=10000),
    zone_1 := Circut("zone_1", 54.967627, 73.347044, radius=9000),
    zone_2 := Circut("zone_2", 54.967627, 73.347044, radius=8000),
    zone_3 := Circut("zone_3", 54.967627, 73.347044, radius=7000),
    zone_4 := Circut("zone_4", 54.967627, 73.347044, radius=6000),
    zone_5 := Circut("zone_5", 54.967627, 73.347044, radius=5000),
    zone_6 := Circut("zone_6", 54.967627, 73.347044, radius=4000),
    zone_7 := Circut("zone_7", 54.967627, 73.347044, radius=3000),
]


# print(distance.geodesic([zone_0.lat, zone_0.long], [zone_1.lat, zone_1.long]).km)