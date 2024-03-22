"""Stream type classes for tap-ms-graph."""
from __future__ import annotations

from tap_ms_graph.client import MSGraphChildStream, MSGraphStream


class GroupsStream(MSGraphStream):
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    odata_context = "groups"
    child_context = {"id": "group_id"}


class GroupMembersStream(MSGraphChildStream):
    parent_stream_type = GroupsStream
    name = "groupMembers"
    path = "/groups/{group_id}/members"
    primary_keys = ["group_id", "id"]
    odata_context = "directoryObjects"
    odata_type = "microsoft.graph.user"

    # TODO: find a way to make this automatic
    parent_context_schema = {
        "group_id": {"type": "string"},
    }


class SubscribedSkusStream(MSGraphStream):
    name = "subscribedSkus"
    path = "/subscribedSkus"
    primary_keys = ["id"]
    odata_context = "subscribedSkus"


class UsersStream(MSGraphStream):
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    odata_context = "users"

class ListsStream(MSGraphStream):
    name = "centre"
    path = "/sites/evolveeducationgroup.sharepoint.com,6b62a68b-7f1f-4e94-8e39-62c0781707d9,eeed0bc0-acbd-44db-a8c2-dcf56fdef467/lists/centre/items?expand=fields"
    primary_keys = ["id"]
    odata_context = "sites"