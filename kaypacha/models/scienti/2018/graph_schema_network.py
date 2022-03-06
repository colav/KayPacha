
# RE_PROYECTO_RED está vacia, no se pueden obtener los proyectos por acá
graph_network = {"MAIN_TABLE": "EN_RED",
                 "SCHEMA_VERSION": 0.1,
                 "GRAPH": [{"EN_RED": [
                     # autor registrante
                     {"KEYS": ["COD_RH"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_RECURSO_HUMANO': None}]},

                     # institucion registrante
                     {"KEYS": ["COD_INST_AVALA/COD_INST"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_INSTITUCION': None}]},
                     # Re-Institucion
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_INSTITUCION_RED': [
                          # instituciones
                          {"KEYS": ["COD_RH", "COD_INSTITUCION/COD_INST"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_INSTITUCION_OTRA': None}
                                        ]}
                      ]}
                     ]},
                     # Re-Autor otros
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_RH_O_RED': [
                          # Autores otros
                          {"KEYS": ["COD_RH/COD_RH_CREA", "COD_RH_OTRO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_RECURSO_HUMANO_OTRO': None}
                                     ]}

                      ]}

                     ]},
                     # Re-Comunidad
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_RED_COMUNIDAD':
                                 # Comunidad
                                 [{"KEYS": ["COD_RH", "COD_COMUNIDAD"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_COMUNIDAD': [
                                       # Municipio
                                       {"KEYS": ["COD_RH_MUNICIPIO", "COD_MUNICIPIO"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'EN_MUNICIPIO': None}]},
                                       # Re-proyecto comunidad
                                       {"KEYS": ["COD_RH", "COD_COMUNIDAD"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'RE_PROYECTO_COMUNIDAD': [
                                               # proyecto
                                               {"KEYS": ["COD_RH", "COD_PROYECTO"],
                                                "DB":"__CVLAC__",
                                                "TABLES":[{"EN_PROYECTO": None}]}
                                           ]}]},
                                       # Re-producto comunidad
                                       {"KEYS": ["COD_RH", "COD_COMUNIDAD"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'RE_PRODUCTO_COMUNIDAD': [
                                               # producto
                                               {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                                                "DB":"__CVLAC__",
                                                "TABLES":[{"EN_PRODUCTO": None}]}
                                           ]}]},

                                   ]}
                                 ]},

                                 ]}
                                ]},

                     # Re-Grupo
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__GRUPLAC__",
                      "TABLES":[{'RE_GRUPO_RH_RED': [
                          # Grupo
                          {"KEYS": ["NRO_ID_GRUPO"],
                           "DB":"__GRUPLAC__",
                           "TABLES":[{"EN_GRUPO_PESQUISA": [
                               # re_institucion
                               {"KEYS": ["NRO_ID_GRUPO"],
                                "DB":"__GRUPLAC__",
                                "TABLES":[{'RE_GRUPO_INSTITUCION': [
                                    # institucion
                                    {"KEYS": ["COD_INST"],
                                     "DB":"__CVLAC__",
                                     "TABLES":[{'EN_INSTITUCION': None}
                                               ]}
                                ]}
                               ]},
                               # Area reconocimiento
                               {"KEYS": ['COD_AREA_CONHEC/COD_AREA_CONOCIMIENTO'],
                                "DB":"__CVLAC__",
                                "TABLES":[
                                   {"EN_AREA_CONOCIMIENTO": None}
                               ]},

                           ]},
                          ]}
                      ]}

                     ]},

                 ]}
                 ]}
