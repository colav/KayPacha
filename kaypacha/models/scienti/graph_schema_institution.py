# notas:
# 1. Las instituciones tienen que ser tomadas de Gruplac por que en institulac hay muy pocas
#    pero todas las de institulac están incluidas den la tabla EN_INSTITUCION de Gruplac
# 2. tabla EN_RECURSO_HUMANO_GR no exsite apesar de que aparece en el diagrama y la doc
# la relación entre grupo y autor sale por la tabla RE_GRUPO_RH usando el campo NRO_ID_CNPQ
# 3. en EN_AVAL_INSTITUCION comentado por que son miles de registros y generan mucho ruido se me a details
# 4. productos avalados produce pymongo.errors.DocumentTooLarge: BSON document too large (27800309 bytes) - the connected server supports BSON document sizes up to 16793598 bytes

graph_institution = {
    "MAIN_TABLE": "EN_INSTITUCION",
    "CHECKPOINT": {"DB": "__GRUPLAC__", "KEYS": ["COD_INST"]},
    "SCHEMA_VERSION": 0.1,
    "GRAPH": [
        {
            "EN_INSTITUCION": [
                # pais
                {
                    "KEYS": ["SGL_PAIS"],
                    "DB": "__CVLAC__",
                    "TABLES": [{"EN_PAIS": None}],
                },
                # departamento
                {
                    "KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                    "DB": "__CVLAC__",
                    "TABLES": [{"EN_DEPARTAMENTO": None}],
                },
                # municipio
                {
                    "KEYS": ["COD_MUNICIPIO", "COD_RH_MUNICIPIO"],
                    "DB": "__CVLAC__",
                    "TABLES": [{"EN_MUNICIPIO": None}],
                },
                # # productos avalados
                # {
                #     "KEYS": ["COD_INST/COD_INSTITUCION"],
                #     "DB": "__INSTITULAC__",
                #     "TABLES": [{"EN_AVAL_INSTITUCION": None}],
                # },
                # grupos
                {
                    "KEYS": ["COD_INST"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [
                        {
                            "RE_GRUPO_INSTITUCION": [
                                {
                                    "KEYS": ["NRO_ID_GRUPO"],
                                    "DB": "__GRUPLAC__",
                                    "TABLES": [
                                        {
                                            "EN_GRUPO_PESQUISA": None
                                        }
                                    ],
                                },
                            ]
                        }
                    ],
                },
            ]
        }
    ],
}
