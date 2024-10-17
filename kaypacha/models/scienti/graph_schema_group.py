# notas:
# 1. Las instituciones tienen que ser tomadas de Gruplac por que en institulac hay muy pocas
#    pero todas las de institulac están incluidas den la tabla EN_INSTITUCION de Gruplac
# 2. tabla EN_RECURSO_HUMANO_GR no exsite apesar de que aparece en el diagrama y la doc
# la relación entre grupo y autor sale por la tabla RE_GRUPO_RH usando el campo NRO_ID_CNPQ
# 3. en EN_AVAL_INSTITUCION comentado por que son miles de registros y generan mucho ruido se me a details
# 4. productos avalados produce pymongo.errors.DocumentTooLarge: BSON document too large (27800309 bytes) - the connected server supports BSON document sizes up to 16793598 bytes

graph_group = {
    "MAIN_TABLE": "EN_GRUPO_PESQUISA",
    "CHECKPOINT": {"DB": "__GRUPLAC__", "KEYS": ["NRO_ID_GRUPO"]},
    "SCHEMA_VERSION": 0.1,
    "GRAPH": [
        {
            "EN_GRUPO_PESQUISA": [
                # lineas de investigación
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [{"EN_LINHA_PESQUISA_GR": None}],
                },
                # productos
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [{"EN_PRODUCTO_GR": None}],
                },
                # evento
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [{"RE_GRUPO_RH_EVENTO": None}],
                },
                #  red
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [{"RE_GRUPO_RH_RED": None}],
                },
                #  colección científica
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [
                        {
                            "EN_COLECCION_CIENTIFICA": [
                                {
                                    "KEYS": [
                                        "NRO_ID_GRUPO",
                                        "SEQ_COLECCION",
                                    ],
                                    "DB": "__GRUPLAC__",
                                    "TABLES": [{"EN_COLECCION_REVISION": None}],
                                },
                                {
                                    "KEYS": [
                                        "NRO_ID_GRUPO",
                                        "SEQ_COLECCION",
                                    ],
                                    "DB": "__GRUPLAC__",
                                    "TABLES": [
                                        {
                                            "RE_COLECCION_RH": [
                                                {
                                                    "KEYS": [
                                                        "NRO_ID_CNPQ",
                                                    ],
                                                    "DB": "__CVLAC__",
                                                    "TABLES": [
                                                        {"EN_RECURSO_HUMANO": None}
                                                    ],
                                                }
                                            ]
                                        }
                                    ],
                                },
                            ]
                        }
                    ],
                },
                # programa minciencias
                {
                    "KEYS": ["COD_PROGRAMA"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [{"EN_PROGRAMA_COLCIENCIAS": None}],
                },
                # programa academico
                {
                    "KEYS": [
                        "NRO_ID_GRUPO",
                        "COD_PROGRAMA_SECUND/SEQ_PROGR_ACAD",
                    ],
                    "DB": "__GRUPLAC__",
                    "TABLES": [
                        {
                            "EN_PROGRAMA_ACADEMICO": [
                                {
                                    "KEYS": [
                                        "NRO_ID_GRUPO",
                                        "SEQ_PROGR_ACAD",
                                    ],
                                    "DB": "__GRUPLAC__",
                                    "TABLES": [{"EN_CURSO_PROGRAMA": None}],
                                },
                            ]
                        }
                    ],
                },
                # autores
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [
                        {
                            "RE_GRUPO_RH": [
                                {
                                    "KEYS": ["NRO_ID_CNPQ"],
                                    "DB": "__CVLAC__",
                                    "TABLES": [{"EN_RECURSO_HUMANO": None}],
                                }
                            ]
                        }
                    ],
                },
                # Area reconocimiento level 2 (tiene 3 niveles máximo) (es con COD_RH_AREA???)
                {
                    "KEYS": [
                        "COD_RH_AREA/COD_RH",
                        "COD_AREA_CONHEC/COD_AREA_CONOCIMIENTO",
                    ],
                    "DB": "__CVLAC__",
                    "TABLES": [
                        {
                            "EN_AREA_CONOCIMIENTO": [
                                # Area reconocimiento level 1
                                {
                                    "KEYS": [
                                        "COD_RH_PADRE/COD_RH",
                                        "COD_AREA_PADRE/COD_AREA_CONOCIMIENTO",
                                    ],
                                    "DB": "__CVLAC__",
                                    "TABLES": [
                                        {
                                            "EN_AREA_CONOCIMIENTO": [
                                                # Area reconocimiento level 0
                                                {
                                                    "KEYS": [
                                                        "COD_RH_PADRE/COD_RH",
                                                        "COD_AREA_PADRE/COD_AREA_CONOCIMIENTO",
                                                    ],
                                                    "DB": "__CVLAC__",
                                                    "TABLES": [
                                                        {"EN_AREA_CONOCIMIENTO": None}
                                                    ],
                                                },
                                            ]
                                        }
                                    ],
                                },
                            ]
                        }
                    ],
                },
                # Proyectos pasando por grupo
                {
                    "KEYS": [
                        "NRO_ID_GRUPO",
                        "SEQ_PRODUCTO/SEQ_PRODUCAO",
                    ],
                    "DB": "__GRUPLAC__",
                    "TABLES": [
                        {
                            "RE_PROYECTO_PRODUCTO_GR": [
                                {
                                    "KEYS": [
                                        "NRO_ID_GRUPO",
                                        "SEQ_PROJETO",
                                    ],
                                    "DB": "__GRUPLAC__",
                                    "TABLES": [{"EN_PROYECTO_GR": None}],
                                }
                            ]
                        }
                    ],
                },
                # instituciones
                {
                    "KEYS": ["NRO_ID_GRUPO"],
                    "DB": "__GRUPLAC__",
                    "TABLES": [
                        {
                            "RE_GRUPO_INSTITUCION": [
                                {
                                    "KEYS": ["COD_INST"],
                                    "DB": "__GRUPLAC__",
                                    "TABLES": [
                                        {
                                            "EN_INSTITUCION": [
                                                # municipio
                                                {
                                                    "KEYS": [
                                                        "COD_RH_MUNICIPIO",
                                                        "COD_MUNICIPIO",
                                                    ],
                                                    "DB": "__CVLAC__",
                                                    "TABLES": [
                                                        {
                                                            "EN_MUNICIPIO": [
                                                                # departamento
                                                                {
                                                                    "KEYS": [
                                                                        "SGL_PAIS",
                                                                        "SGL_DEPARTAMENTO",
                                                                    ],
                                                                    "DB": "__CVLAC__",
                                                                    "TABLES": [
                                                                        {
                                                                            "EN_DEPARTAMENTO": [
                                                                                # pais
                                                                                {
                                                                                    "KEYS": [
                                                                                        "SGL_PAIS"
                                                                                    ],
                                                                                    "DB": "__CVLAC__",
                                                                                    "TABLES": [
                                                                                        {
                                                                                            "EN_PAIS": None
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
                                                },
                                            ]
                                        }
                                    ],
                                }
                            ]
                        }
                    ],
                },
            ]
        }
    ],
}
