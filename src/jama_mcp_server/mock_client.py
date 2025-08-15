import logging

logger = logging.getLogger(__name__)


class MockJamaClient:
    """A mock implementation of the JamaClient for testing without a real Jama instance."""

    def __init__(self):
        # Seed with a few example items
        self._items = {
            "123": {
                "id": 123,
                "documentKey": "MOCK-1",
                "fields": {"name": "Mock Item 123", "description": "A sample item."},
            },
            "456": {
                "id": 456,
                "documentKey": "MOCK-2",
                "fields": {"name": "Another Mock Item", "description": "Details here."},
            },
            "789": {
                "id": 789,
                "documentKey": "MOCK-3",
                "fields": {"name": "Child Item 1", "description": "Child of 123"},
            },
            "790": {
                "id": 790,
                "documentKey": "MOCK-4",
                "fields": {"name": "Child Item 2", "description": "Another child of 123"},
            },
        }
        self._next_id = 1000

    # --- Read Operations ---

    def get_projects(self):
        logger.info("MOCK: get_projects() called")
        return [
            {"id": 1, "name": "Mock Project Alpha", "projectKey": "MPA"},
            {"id": 2, "name": "Mock Project Beta", "projectKey": "MPB"},
        ]

    def get_item(self, item_id: str):
        logger.info(f"MOCK: get_item(item_id='{item_id}') called")
        item = self._items.get(str(item_id))
        if item:
            return item
        logger.warning(f"MOCK: Item ID {item_id} not found.")
        return None

    def get_available_endpoints(self):
        logger.info("MOCK: get_available_endpoints() called")
        return {"data": [{"path": "/mock", "method": "GET"}]}

    def get_items(self, project_id: str = None):
        if project_id is not None:
            logger.info(f"MOCK: get_items(project_id='{project_id}') called")
            if project_id == "1":
                item = self.get_item("123")
                return [item] if item else []
            if project_id == "2":
                item = self.get_item("456")
                return [item] if item else []
            logger.warning(f"MOCK: Project ID {project_id} not found for get_items.")
            return []
        logger.warning("MOCK: get_items() called without project_id, returning empty list.")
        return []

    def get_item_children(self, item_id: str):
        logger.info(f"MOCK: get_item_children(item_id='{item_id}') called")
        if item_id == "123":
            return [self._items["789"], self._items["790"]]
        logger.warning(f"MOCK: Parent item ID '{item_id}' not found or has no children.")
        return []

    def get_relationships(self, project_id: str):
        logger.info(f"MOCK: get_relationships(project_id='{project_id}') called")
        if project_id == "1":
            return [
                {"id": 101, "fromItem": 123, "toItem": 789, "relationshipType": 1},
                {"id": 102, "fromItem": 790, "toItem": 123, "relationshipType": 2},
            ]
        return []

    def get_relationship(self, relationship_id: str):
        logger.info(f"MOCK: get_relationship(relationship_id='{relationship_id}') called")
        if relationship_id == "101":
            return {"id": 101, "fromItem": 123, "toItem": 789, "relationshipType": 1}
        return None

    def get_items_upstream_relationships(self, item_id: str):
        logger.info(f"MOCK: get_items_upstream_relationships(item_id='{item_id}') called")
        if item_id == "789":
            return [{"id": 101, "fromItem": 123, "toItem": 789, "relationshipType": 1}]
        return []

    def get_items_downstream_relationships(self, item_id: str):
        logger.info(f"MOCK: get_items_downstream_relationships(item_id='{item_id}') called")
        if item_id == "123":
            return [{"id": 101, "fromItem": 123, "toItem": 789, "relationshipType": 1}]
        return []

    def get_items_upstream_related(self, item_id: str):
        logger.info(f"MOCK: get_items_upstream_related(item_id='{item_id}') called")
        if item_id == "789":
            return [self.get_item("123")]
        return []

    def get_items_downstream_related(self, item_id: str):
        logger.info(f"MOCK: get_items_downstream_related(item_id='{item_id}') called")
        if item_id == "123":
            return [self.get_item("789")]
        return []

    def get_item_types(self):
        logger.info("MOCK: get_item_types() called")
        return [
            {"id": 10, "name": "Requirement", "typeKey": "REQ"},
            {"id": 11, "name": "Test Case", "typeKey": "TC"},
        ]

    def get_item_type(self, item_type_id: str):
        logger.info(f"MOCK: get_item_type(item_type_id='{item_type_id}') called")
        if item_type_id == "10":
            return {"id": 10, "name": "Requirement", "typeKey": "REQ"}
        return None

    def get_pick_lists(self):
        logger.info("MOCK: get_pick_lists() called")
        return [{"id": 20, "name": "Priority"}, {"id": 21, "name": "Status"}]

    def get_pick_list(self, pick_list_id: str):
        logger.info(f"MOCK: get_pick_list(pick_list_id='{pick_list_id}') called")
        if pick_list_id == "20":
            return {"id": 20, "name": "Priority"}
        return None

    def get_pick_list_options(self, pick_list_id: str):
        logger.info(f"MOCK: get_pick_list_options(pick_list_id='{pick_list_id}') called")
        if pick_list_id == "20":
            return [
                {"id": 201, "name": "High"},
                {"id": 202, "name": "Medium"},
                {"id": 203, "name": "Low"},
            ]
        return []

    def get_pick_list_option(self, pick_list_option_id: str):
        logger.info(f"MOCK: get_pick_list_option(pick_list_option_id='{pick_list_option_id}') called")
        if pick_list_option_id == "201":
            return {"id": 201, "name": "High"}
        return None

    def get_tags(self, project: str):
        logger.info(f"MOCK: get_tags(project='{project}') called")
        if project == "1":
            return [{"id": 301, "name": "UI"}, {"id": 302, "name": "Backend"}]
        return []

    def get_tagged_items(self, tag_id: str):
        logger.info(f"MOCK: get_tagged_items(tag_id='{tag_id}') called")
        if tag_id == "301":
            return [self.get_item("123")]
        return []

    def get_test_cycle(self, test_cycle_id: str):
        logger.info(f"MOCK: get_test_cycle(test_cycle_id='{test_cycle_id}') called")
        if test_cycle_id == "501":
            return {"id": 501, "name": "Cycle 1", "startDate": "2025-01-01", "endDate": "2025-01-31"}
        return None

    def get_testruns(self, test_cycle_id: str):
        logger.info(f"MOCK: get_testruns(test_cycle_id='{test_cycle_id}') called")
        if test_cycle_id == "501":
            return [
                {"id": 601, "name": "Run 1", "status": "PASSED"},
                {"id": 602, "name": "Run 2", "status": "FAILED"},
            ]
        return []

    # --- Write Operations ---

    def post_item(self, project, item_type_id, child_item_type_id, location, fields, global_id=None):
        logger.info(
            "MOCK: post_item(project=%s, item_type_id=%s, child_item_type_id=%s, location=%s) called",
            project,
            item_type_id,
            child_item_type_id,
            location,
        )
        item_id = self._next_id
        self._next_id += 1
        new_item = {"id": item_id, "documentKey": f"MOCK-{item_id}", "fields": fields}
        self._items[str(item_id)] = new_item
        return item_id


