# notas:
# N/A

graph_publisher_other = {
    "MAIN_TABLE": "EN_EDITORIAL_OTRO",
    "CHECKPOINT": {"DB": "__CVLAC__", "KEYS": ["COD_EDITORIAL", "COD_RH"]},
    "SCHEMA_VERSION": 0.1,
    "GRAPH": [
        {
            "EN_EDITORIAL_OTRO": [
                # revista otra
                {
                    "KEYS": ["COD_EDITORIAL/COD_EDITORIAL_OTRO","COD_RH"],
                    "DB": "__CVLAC__",
                    "TABLES": [
                        {
                            "EN_REVISTA_OTRA": [
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
