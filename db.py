from typing import Any, Dict, List, Tuple, Type

from db_def import ConfigInterface, DBInterface

# ----------------- 数据定义 -----------------


class DemoDB(DBInterface):
    def __init__(self):
        super().__init__()
        self.int_val = 1
        self.bool_val = True


class FirstRunDB(DBInterface):
    def __init__(self):
        super().__init__()

    def get_version(self) -> str:
        # 2.0.0     修改字段update为_update，废弃原有数据
        return "2.0.0"


class CacheDB(DBInterface):
    def __init__(self):
        super().__init__()

        self.cache: Dict[str, CacheInfo] = {}

    def dict_fields_to_fill(self) -> List[Tuple[str, Type[ConfigInterface]]]:
        return [("cache", CacheInfo)]


class CacheInfo(DBInterface):
    def __init__(self):
        super().__init__()

        self.value: Any = None


if __name__ == "__main__":
    print(DBInterface())
    print(DemoDB())
