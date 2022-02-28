# Scienti data model 2018
# SCHEMA version for modification on the relations, it is vertioned as well
graph_schema = {"SCIENTI_MODEL": 2018}
graph_schema["MODELS"] = []
graph_product = {"MAIN_TABLE": "EN_PRODUCTO",
                 "SCHEMA_VERSION": 0.1,
                 "GRAPH": [{"EN_PRODUCTO": [
                     # autor registrante
                     {"KEYS": ["COD_RH"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_RECURSO_HUMANO': None}]},
                     # institucion registrante
                     {"KEYS": ["COD_INST_AVALA/COD_INST"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_INSTITUCION': None}]},
                     # Prod type
                     # Prod type level 3
                     {"KEYS": ["COD_TIPO_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_TIPO_PRODUCTO': [
                             # Prod type level 2
                             {"KEYS": ["COD_TIPO_PRODUCTO_PADRE/COD_TIPO_PRODUCTO"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_TIPO_PRODUCTO': [
                                  # Prod type level 1
                                  {"KEYS": ["COD_TIPO_PRODUCTO_PADRE/COD_TIPO_PRODUCTO"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_TIPO_PRODUCTO': [
                                       # Prod type level 0
                                       {"KEYS": ["COD_TIPO_PRODUCTO_PADRE/COD_TIPO_PRODUCTO"],
                                        "DB":"__CVLAC__",
                                        "TABLES":[{'EN_TIPO_PRODUCTO': None}
                                                  ]}
                                   ]}
                                  ]}

                              ]}
                             ]},

                         ]}
                     ]},
                     # Proyecto diecto de producto
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'RE_PROYECTO_PRODUCTO':
                                    [{"KEYS": ["COD_RH", "COD_PROYECTO"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[{'EN_PROYECTO': None}]},

                                     ]}]},

                     # Grupo x Producto
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__GRUPLAC__",
                      "TABLES":[{'EN_PRODUCTO_GR': [
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
                          ]},
                          # Proyectos pasando por grupo
                          {"KEYS": ['NRO_ID_GRUPO', 'SEQ_PRODUCTO/SEQ_PRODUCAO'],
                              "DB":"__GRUPLAC__",
                              "TABLES":[
                              {"RE_PROYECTO_PRODUCTO_GR": [{"KEYS": ["NRO_ID_GRUPO", "SEQ_PROJETO"],
                                                           "DB":"__GRUPLAC__",
                                                            "TABLES":[
                                  {"EN_PROYECTO_GR": None}
                              ]}
                              ]}
                          ]},
                      ]}
                     ]},
                     # Recurso humano otro
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'RE_PRODUCTO_RECURSO_HUM_OTRO': [{"KEYS": ["COD_RH/COD_RH_CREA", "COD_RH_OTRO"],
                                                                      "DB":"__CVLAC__",
                                                                      "TABLES":[{'EN_RECURSO_HUMANO_OTRO': None}
                                                                                ]}
                                                                     ]}
                                   ]},
                     # Prod tecnica (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_TECNICA':
                                    [{"KEYS": ["COD_RH", "COD_PRODUCTO"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[
                                        # Patente
                                        {'EN_PATENTE': None},
                                        # Producto Tecnilogico
                                        {'EN_PROD_TECNOLOGICO': None},
                                        # secreto industrial
                                        {'EN_SECRETO_INDUSTRIAL': None},
                                        # software
                                        {'EN_PROD_SOFTWARE': None},
                                        # Registro
                                        {'EN_REGISTRO': None},
                                        # prod vegetal
                                        {'EN_PROD_VEGETAL': None},

                                    ]},

                                    ]}
                                   ]},
                     #                                    # Prod artistica (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_PROD_ARTISTICA': [
                          # prod artistica detalles
                          {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PROD_ARTISTICA_DETALLE': None}
                                     ]}
                      ]}
                     ]},
                     # Prod obra artistica (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_TESIS_ORIENTADA': None}]},
                     # Tesis orientada (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_TESIS_ORIENTADA': None}]},
                     # Producion audiovisual (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_AUDIOVISUAL': None}]},
                     # Partitura (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_AUDIOVISUAL': None}]},
                     # Capitulo libro (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_CAPITULO_LIBRO': None}]},
                     # libro (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_LIBRO': None}]},
                     # Prod Articulos (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_ARTICULO': [
                             # revista
                             {"KEYS": ["COD_REVISTA"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_REVISTA': [
                                  # editorial
                                  {"KEYS": ["COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL': None}
                                             ]}
                              ]}
                             ]},
                             # revista otra
                             {"KEYS": ["COD_RH", "COD_REVISTA_OTRO/COD_REVISTA"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_REVISTA_OTRA': [
                                  # Editorial
                                  {"KEYS": ["COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL': None}
                                             ]},
                                  # Editorial otro
                                  {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL_OTRO': None}
                                             ]},
                              ]}
                             ]},
                         ]}
                     ]},
                     # Prod biblio (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_PROD_BIBLIO': [
                          # revista
                          {"KEYS": ["COD_REVISTA"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_REVISTA': [
                               # editorial
                               {"KEYS": ["COD_EDITORIAL"],
                                "DB":"__CVLAC__",
                                "TABLES":[{'EN_EDITORIAL': None}
                                          ]}
                           ]}
                          ]},
                          # revista otra
                          {"KEYS": ["COD_RH", "COD_REVISTA_OTRO/COD_REVISTA"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_REVISTA_OTRA': [
                                  # Editorial
                                  {"KEYS": ["COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL': None}
                                             ]},
                                  # Editorial otro
                                  {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL_OTRO': None}
                                             ]},
                              ]}
                          ]},
                      ]}
                     ]},
                     # Re-Sector Apliación
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PRODUCTO_SECTOR_APL': [
                          # sector aplicación nivel 2
                          {"KEYS": ["COD_SECTOR_APLICACION"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_SECTOR_APLICACION': [
                               # sector aplicación nivel 1
                               {"KEYS": ["COD_SECT_APLIC_PADRE/COD_SECTOR_APLICACION"],
                                "DB":"__CVLAC__",
                                "TABLES":[{'EN_SECTOR_APLICACION': None}
                                          ]}
                           ]}
                          ]}
                      ]}

                     ]},
                     # Re-Palabra clave
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PRODUCTO_PALABRA_CLA': [
                          # Palabra clave
                          {"KEYS": ["COD_RH", "COD_PALABRA_CLAVE"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PALABRA_CLAVE': None}
                                     ]}
                      ]}

                     ]}

                 ]}
                 ]}


graph_schema["MODELS"].append(graph_product)

