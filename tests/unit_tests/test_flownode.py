from pymetrix.endpoints import Endpoint, EndpointType

from pymetrix.flow import (
    FlowNode,
    FlowNodeType,
)


def foo1():
    print("Foo1")


def test_flowNode_creation():
    ep1: EndpointType = Endpoint(endpoint="Foo1", id=foo1)
    node1: FlowNodeType = FlowNode(ep1, name="Node1")

    assert isinstance(node1.__str__(), str)


def test_init():
    ep1: EndpointType = Endpoint(endpoint="Foo1", id=foo1)
    node1: FlowNodeType = FlowNode(ep1, name="Node1")

    assert node1.children == [] and node1.parents == []


def test_serialize():
    ep1: EndpointType = Endpoint(endpoint="Foo1", id=foo1)
    node1: FlowNodeType = FlowNode(ep1, name="Node1")

    assert (
        isinstance(node1.serialize, dict)
        and [
            "node_id",
            "parents",
            "children",
            "endpoint",
        ]
        == list(node1.serialize.keys())
    )


def test_gethits():
    ep1: EndpointType = Endpoint(endpoint="Foo1", id=foo1)
    node1: FlowNodeType = FlowNode(ep1, name="Node1")

    assert (
        isinstance(node1.gethits, dict)
        and [
            "id",
            "hits",
            "time",
            "callers",
        ]
        == list(node1.gethits.keys())
    )


def test_visualize():
    ep1: EndpointType = Endpoint(endpoint="Foo1", id=foo1)
    node1: FlowNodeType = FlowNode(ep1, name="Node1")

    assert len(node1.visualize) == 0