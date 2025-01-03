from .graph_fields_product import product_fields
from .graph_fields_network import network_fields
from .graph_fields_project import project_fields
from .graph_fields_event import event_fields
from .graph_fields_patent import patent_fields
from .graph_fields_endorsement import endorsement_fields
from .graph_fields_author import author_fields
from .graph_fields_institution import institution_fields
from .graph_fields_group import group_fields
from .graph_fields_publisher import publisher_fields
from .graph_fields_publisher_other import publisher_other_fields

graph_fields = {}

# adding fields for every main entity
graph_fields["EN_PRODUCTO"] = product_fields
graph_fields["EN_RED"] = network_fields
graph_fields["EN_PROYECTO"] = project_fields
graph_fields["EN_EVENTO"] = event_fields
graph_fields["EN_PATENTE"] = patent_fields
graph_fields["EN_AVAL_INSTITUCION"] = endorsement_fields
graph_fields["EN_RECURSO_HUMANO"] = author_fields
graph_fields["EN_INSTITUCION"] = institution_fields
graph_fields["EN_GRUPO_PESQUISA"] = group_fields
graph_fields["EN_EDITORIAL"] = publisher_fields
graph_fields["EN_EDITORIAL_OTRO"] = publisher_other_fields
