# notas:
# N/A

graph_publisher = {
    "MAIN_TABLE": "EN_EDITORIAL",
    "CHECKPOINT": {"DB": "__CVLAC__", "KEYS": ["COD_EDITORIAL"]},
    "SCHEMA_VERSION": 0.1,
    "GRAPH": [
        {
            "EN_EDITORIAL": [
                # revista
                {
                    "KEYS": ["COD_EDITORIAL"],
                    "DB": "__CVLAC__",
                    "TABLES": [
                        {
                            "EN_REVISTA": [
                                # pais
                                {
                                    "KEYS": ["SGL_PAIS"],
                                    "DB": "__CVLAC__",
                                    "TABLES": [{"EN_PAIS": None}],
                                }
                            ]
                        }
                    ],
                },
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
                                                    "KEYS": ["SGL_PAIS"],
                                                    "DB": "__CVLAC__",
                                                    "TABLES": [{"EN_PAIS": None}],
                                                },
                                            ]
                                        }
                                    ],
                                },
                            ]
                        }
                    ],
                },
                # instituciones
                {
                    "KEYS": ["ID_INSTITUCION"],
                    "DB": "__CVLAC__",
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
                },
            ]
        }
    ],
}
