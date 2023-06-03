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
                        {"SIIU_PROYECTO": None}
                    ]
                },

            ]
        }
    ]
}
