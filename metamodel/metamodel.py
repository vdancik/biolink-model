# Auto generated from /Users/solbrig/git/hsolbrig/biolink-model/meta.yaml by pythongen.py version: 0.0.1
# Generation date: 2018-05-29 17:20
# Schema: metamodel
#
# id: http://bioentity.io/json-schema/meta.json
# description: Metamodel for biolink schema
# license: https://creativecommons.org/publicdomain/zero/1.0/

import datetime
from typing import Optional, List, Union, Dict, NewType
from dataclasses import dataclass
from metamodel.metamodelcore import Root, empty_list, empty_dict

# Class references
ExampleName = NewType("ExampleName", str)
ElementName = NewType("ElementName", str)
DefinitionName = NewType("DefinitionName", str)
SlotDefinitionName = NewType("SlotDefinitionName", str)
ClassDefinitionName = NewType("ClassDefinitionName", str)
TypeDefinitionName = NewType("TypeDefinitionName", str)
SchemaDefinitionName = NewType("SchemaDefinitionName", str)
SchemaDefinitionId = NewType("SchemaDefinitionId", str)

# Type references


@dataclass
class Example(Root):
    """
    example of usage
    """
    value: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Element(Root):
    """
    root of all described things
    """
    name: ElementName
    singular_name: Optional[str] = None
    description: Optional[str] = None
    note: Optional[str] = None
    comment: Optional[str] = None
    examples: List[Union[dict, Example]] = empty_list()
    prefixes: List[str] = empty_list()
    aliases: List[str] = empty_list()
    mappings: List[str] = empty_list()
    id_prefixes: List[str] = empty_list()
    in_subset: List[str] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        self.examples = [v if isinstance(v, Example) else Example(**({} if v is None else v)) for v in self.examples]


@dataclass
class Definition(Element):
    """
    definition base class
    """
    name: DefinitionName = None
    is_a: Optional[DefinitionName] = None
    mixin: bool = False
    mixins: List[DefinitionName] = empty_list()
    abstract: bool = False
    local_names: List[str] = empty_list()
    union_of: List[DefinitionName] = empty_list()
    subclass_of: Optional[DefinitionName] = None
    values_from: List[str] = empty_list()


@dataclass
class SlotDefinition(Definition):
    """
    A property or slot
    """
    name: SlotDefinitionName = None
    multivalued: bool = False
    domain: Optional[ClassDefinitionName] = None
    range: Optional[ElementName] = None
    required: bool = False
    inlined: bool = False
    primary_key: bool = False
    identifier: bool = False
    definitional: bool = False
    alias: Optional[str] = None
    path: Optional[str] = None
    subproperty_of: Optional[str] = None
    symmetric: bool = False
    inverse: Optional[SlotDefinitionName] = None
    is_class_field: bool = False


@dataclass
class ClassDefinition(Definition):
    """
    A class or interface
    """
    name: ClassDefinitionName = None
    defining_slots: List[SlotDefinitionName] = empty_list()
    slots: List[SlotDefinitionName] = empty_list()
    slot_usage: Dict[SlotDefinitionName, Union[dict, SlotDefinition]] = empty_dict()
    apply_to: Optional[ClassDefinitionName] = None

    def _fix_elements(self):
        super()._fix_elements()
        for k, v in self.slot_usage.items():
                if not isinstance(v, SlotDefinition):
                    self.slot_usage[k] = SlotDefinition(name=k, **({} if v is None else v))


@dataclass
class TypeDefinition(Element):
    """
    A type definition
    """
    name: TypeDefinitionName = None
    typeof: Optional[str] = None


@dataclass
class SchemaDefinition(Definition):
    """
    A collection of definitions
    """
    name: SchemaDefinitionName = None
    id: SchemaDefinitionId = None
    imports: List[str] = empty_list()
    license: Optional[str] = None
    types: Dict[TypeDefinitionName, Union[dict, TypeDefinition]] = empty_dict()
    slots: Dict[SlotDefinitionName, Union[dict, SlotDefinition]] = empty_dict()
    classes: Dict[ClassDefinitionName, Union[dict, ClassDefinition]] = empty_dict()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is None:
            raise ValueError(f"id must be supplied")
        for k, v in self.types.items():
                if not isinstance(v, TypeDefinition):
                    self.types[k] = TypeDefinition(name=k, **({} if v is None else v))
        for k, v in self.slots.items():
                if not isinstance(v, SlotDefinition):
                    self.slots[k] = SlotDefinition(name=k, **({} if v is None else v))
        for k, v in self.classes.items():
                if not isinstance(v, ClassDefinition):
                    self.classes[k] = ClassDefinition(name=k, **({} if v is None else v))
