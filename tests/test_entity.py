from pyannotations import annotations

from persipy import entity


def test_entity_annotation():
    @entity
    class MyEntity:
        pass

    assert list(annotations.get_annotations_of_class(MyEntity)) == ['persipy.entity']
