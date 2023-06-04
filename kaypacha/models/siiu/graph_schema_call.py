graph_call = {
    "MAIN_TABLE": "SIIU_CONVOCATORIA",
    "CHECKPOINT": {"DB": "BUPP", "KEYS": ["IDENTIFICADOR"]},
    "SCHEMA_VERSION": 0.1,
    "GRAPH": [
        {
            "SIIU_CONVOCATORIA": [
                {
                    "KEYS": ["IDENTIFICADOR/CONVOCATORIA"],
                    "DB":"BUPP",
                    "TABLES":[
                        {"SIIU_PROYECTO": [{
                            "KEYS": ["MODALIDAD_CONVOCATORIA/IDENTIFICADOR"],
                            "DB":"BUPP",
                            "TABLES":[
                                {"SIIU_MODALIDAD_CONVOCATORIA": None}
                            ]
                        }
                        ]}
                    ]
                },
                {
                    "KEYS": ["IDENTIFICADOR/CONVOCATORIA"],
                    "DB":"BUPP",
                    "TABLES":[
                        {"SIIU_FECHA_INTERMEDIA": [{
                            "KEYS": ["IDENTIFICADOR"],
                            "DB":"BUPP",
                            "TABLES":[
                                {"SIIU_FECHA_PROCESO_SELECCION": [{
                                    "KEYS": ["ETAPA_PROCESO_SELECCION/IDENTIFICADOR"],
                                    "DB":"BUPP",
                                    "TABLES":[
                                        {"SIIU_ETAPA_PROCESO_SELECCION": [{
                                            "KEYS": ["INSTANCIA_ADMINISTRATIVA/IDENTIFICADOR"],
                                            "DB":"BUPP",
                                            "TABLES":[
                                                {"SIIU_INSTANCIA_ADMINISTRATIVA": [{
                                                    "KEYS": ["INSTANCIA_SUPERIOR/IDENTIFICADOR"],
                                                    "DB":"BUPP",
                                                    "TABLES":[{
                                                        "SIIU_INSTANCIA_ADMINISTRATIVA": [{
                                                            "KEYS": ["INSTANCIA_SUPERIOR/IDENTIFICADOR"],
                                                            "DB":"BUPP",
                                                            "TABLES":[{
                                                                "SIIU_INSTANCIA_ADMINISTRATIVA": [{
                                                                    "KEYS": ["INSTANCIA_SUPERIOR/IDENTIFICADOR"],
                                                                    "DB":"BUPP",
                                                                    "TABLES":[{
                                                                        "SIIU_INSTANCIA_ADMINISTRATIVA": None
                                                                    }]
                                                                }]
                                                            }]
                                                        }]
                                                    }]
                                                }]
                                                }]
                                        }]
                                        }]
                                }]
                                }]
                        }]
                        }]
                },
            ]
        }
    ]
}
