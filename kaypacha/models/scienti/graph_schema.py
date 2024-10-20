# SCHEMA version for modification on the relations, it is vertioned as well
from .graph_schema_product import graph_product
from .graph_schema_network import graph_network
from .graph_schema_project import graph_project
from .graph_schema_event import graph_event
from .graph_schema_patent import graph_patent
from .graph_schema_endorsement import graph_endorsement
from .graph_schema_author import graph_author
from .graph_schema_institution import graph_institution
from .graph_schema_group import graph_group
from .graph_schema_publisher import graph_publisher
from .graph_schema_publisher_other import graph_publisher_other


graph_schema = {"SCIENTI_MODEL": 2023}
graph_schema["MODELS"] = {}

graph_schema["MODELS"]["network"] = graph_network
graph_schema["MODELS"]["product"] = graph_product
graph_schema["MODELS"]["project"] = graph_project
graph_schema["MODELS"]["event"] = graph_event
graph_schema["MODELS"]["patent"] = graph_patent
graph_schema["MODELS"]["endorsement"] = graph_endorsement
graph_schema["MODELS"]["author"] = graph_author
graph_schema["MODELS"]["institution"] = graph_institution
graph_schema["MODELS"]["group"] = graph_group
graph_schema["MODELS"]["publisher"] = graph_publisher
graph_schema["MODELS"]["publisher_other"] = graph_publisher_other
