# RE_PROYECTO_RED está vacia, no se pueden obtener los proyectos por acá
graph_project = {"MAIN_TABLE": "EN_PROYECTO",
                 "CHECKPOINT": {"DB": "__CVLAC__", "KEYS": ["COD_RH", "COD_PROYECTO"]},
                 "SCHEMA_VERSION": 0.1,
                 "GRAPH": [{"EN_PROYECTO": [
                     # autor registrante
                     {"KEYS": ["COD_RH"],
                      "DB":"__CVLAC__",
                      "TABLES":[
                          {'EN_RECURSO_HUMANO': [
                              # municipio
                              {"KEYS": ["COD_RH_MUN_NACIM/COD_RH_MUNICIPIO", "COD_MUN_NACIM/COD_MUNICIPIO"],
                                  "DB":"__CVLAC__",
                                  "TABLES":[{'EN_MUNICIPIO': [
                                      # departamento
                                      {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                                       "DB":"__CVLAC__",
                                       "TABLES":[{'EN_DEPARTAMENTO': [
                                           # pais
                                           {"KEYS": ["SGL_PAIS"],
                                            "DB":"__CVLAC__",
                                            "TABLES":[{'EN_PAIS': None}]},

                                       ]}]},
                                  ]}]},
                              # level of studies
                              {"KEYS": ["COD_NIVEL_FORMACION"],
                                  "DB":"__CVLAC__",
                                  "TABLES":[{'EN_NIVEL_FORMACION': None}]},
                          ]},
                     ]},
                     # Re-Recurso humano otro
                     {"KEYS": ["COD_RH", "COD_PROYECTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PROYECTO_REC_HUMANO_OTRO': [
                          # Autores otros
                          {"KEYS": ["COD_RH/COD_RH_CREA", "COD_RH_OTRO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_RECURSO_HUMANO_OTRO': None}
                                     ]}
                      ]}
                     ]},

                     # institucion registrante
                     {"KEYS": ["COD_INST_AVALA/COD_INST"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_INSTITUCION': [
                          # pais
                          {"KEYS": ["SGL_PAIS"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PAIS': None}]},

                      ]}]},
                     # Re-Institucion
                     {"KEYS": ["COD_RH", "COD_PROYECTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PROYECTO_INSTITUCION':
                                 [
                                     # tipo de financiación (NO ESTA FUNCIONANDO ESTE!)
                                     {"KEYS": ["COD_TIPO_FINANCIACION"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[{'EN_TIPO_FINANCIACION': None}
                                                ]},
                                     # institucion
                                     {"KEYS": ["COD_INST"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[{'EN_INSTITUCION': [
                                          # pais
                                          {"KEYS": ["SGL_PAIS"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'EN_PAIS': None}]},
                                      ]}
                                     ]},

                                     # instituciones
                                     {"KEYS": ["COD_RH", "COD_INST_OTRO/COD_INST"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[
                                         # insticiones otras
                                         {'EN_INSTITUCION_OTRA': [
                                             # municipio
                                             {"KEYS": ["COD_RH_MUNICIPIO", "COD_MUNICIPIO"],
                                              "DB":"__CVLAC__",
                                              "TABLES":[{'EN_MUNICIPIO': [
                                                  # departamento
                                                  {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                                                   "DB":"__CVLAC__",
                                                   "TABLES":[{'EN_DEPARTAMENTO': [
                                                       # pais
                                                       {"KEYS": ["SGL_PAIS"],
                                                        "DB":"__CVLAC__",
                                                        "TABLES":[{'EN_PAIS': None}]},

                                                   ]}]},
                                              ]}]},

                                         ]},
                                     ]},

                                 ]}
                                ]},
                     # Re-proyecto producto
                     {"KEYS": ["COD_RH", "COD_PROYECTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PROYECTO_PRODUCTO': [
                          # producto  (aca muere por que producto es tabla principal)
                          {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PRODUCTO': None}
                                     ]}
                      ]}
                     ]},
                     # Re-proyecto evento
                     {"KEYS": ["COD_RH", "COD_PROYECTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_EVENTO_PROYECTO': [
                          # evento (aca muere por que evento es tabla principal)
                          {"KEYS": ["COD_RH", "COD_EVENTO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_EVENTO': None}
                                     ]}
                      ]}
                     ]},


                 ]}
                 ]}
