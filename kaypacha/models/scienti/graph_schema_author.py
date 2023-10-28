# notas:
# 1. COD_NIVEL_FORMACION: no funciona tomandolo de la tabla EN_RECURSO_HUMANO
# 2. tabla EN_RECURSO_HUMANO_GR no exsite apesar de que aparece en el diagrama y la doc
# la relación entre grupo y autor sale por la tabla RE_GRUPO_RH usando el campo NRO_ID_CNPQ
graph_author = {"MAIN_TABLE": "EN_RECURSO_HUMANO",
                "CHECKPOINT": {"DB": "__CVLAC__", "KEYS": ["COD_RH"]},
                "SCHEMA_VERSION": 0.1,
                "GRAPH": [{"EN_RECURSO_HUMANO": [
                    # municipio
                    {"KEYS": ["COD_RH_MUN_NACIM/COD_RH_MUNICIPIO", "COD_MUN_NACIM/COD_MUNICIPIO"],
                     "DB": "__CVLAC__",
                     "TABLES": [{'EN_MUNICIPIO': [
                          # departamento
                          {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                           "DB": "__CVLAC__",
                           "TABLES": [{'EN_DEPARTAMENTO': [
                               # pais
                               {"KEYS": ["SGL_PAIS"],
                                "DB": "__CVLAC__",
                                "TABLES": [{'EN_PAIS': None}]},

                           ]}]},
                          ]}]},
                    # nationality
                    {"KEYS": ["TPO_NACIONALIDAD"],
                     "DB": "__CVLAC__",
                     "TABLES": [{'EN_TIPO_NACIONALIDAD': None}]},
                    # studies trajectory
                    {"KEYS": ["COD_RH"],
                     "DB": "__CVLAC__",
                     "TABLES": [{'EN_TRAYECTORIA_ESCOLAR': [
                         {"KEYS": ["COD_RH_PROG_ACAD/COD_RH", "COD_PROGRAMA_ACADEMICO"],
                           "DB": "__CVLAC__",
                           "TABLES": [
                             # academic program
                             {'EN_PROGRAMA_ACADEMICO': [
                                 {"KEYS": ["COD_NIVEL_FORMACION"],
                                  "DB": "__CVLAC__",
                                  "TABLES": [
                                     # studies level
                                     {'EN_NIVEL_FORMACION': None}
                                 ]}
                             ]}
                         ]},
                         {"KEYS": ["COD_INST"],
                          "DB": "__CVLAC__",
                          "TABLES": [
                             # institution
                             {'EN_INSTITUCION': None
                              }]}
                     ]},
                    ]},
                    # profesinal trajectory
                    {"KEYS": ["COD_RH"],
                     "DB": "__CVLAC__",
                     "TABLES": [{'EN_TRAYECTORIA_PROFESIONAL': [
                         # admin activities
                         {"KEYS": ["COD_RH", "COD_TRAY_PROFESIONAL"],
                           "DB": "__CVLAC__",
                           "TABLES": [{'EN_ACT_ADMINISTRACION': None}]},
                         # research activities
                         {"KEYS": ["COD_RH", "COD_TRAY_PROFESIONAL"],
                          "DB": "__CVLAC__",
                          "TABLES": [{'EN_ACT_INVESTIGACION': None}]},
                         # teaching activities
                         {"KEYS": ["COD_RH", "COD_TRAY_PROFESIONAL"],
                          "DB": "__CVLAC__",
                          "TABLES": [{'EN_ACT_DOCENCIA': None}]},

                     ]}]},
                    # relación entre grupo and autor
                    # los autores pueden estar en varios grupos
                    # tabla EN_RECURSO_HUMANO_GR no exsite,
                    # apesar de que aparece en el diagrama y la doc
                    {"KEYS": ["NRO_ID_CNPQ"],
                     "DB": "__GRUPLAC__",
                     "TABLES": [{'RE_GRUPO_RH': [
                         # group
                         {"KEYS": ["NRO_ID_GRUPO"],
                          "DB": "__GRUPLAC__",
                          "TABLES": [{'EN_GRUPO_PESQUISA': None}]},

                     ]}]},
                    # product
                    {"KEYS": ["COD_RH"],
                     "DB": "__CVLAC__",
                     "TABLES": [{'EN_PRODUCTO': None}]},

                ]}
                ]}
