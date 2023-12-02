from __future__ import annotations

from data_struct import ConfigInterface


class DemoDao(ConfigInterface):
    def __init__(self):
        # 普通值
        self.normal_value = "3"
        # list，且元素也需要自动解析
        self.list_value: list[DemoSubDao] = []
        # dict，且其value也需要自动解析
        self.dict_value: dict[str, DemoSubDao] = {}

    def fields_to_fill(self):
        return [
            ("list_value", DemoSubDao),
        ]

    def dict_fields_to_fill(self) -> list[tuple[str, type[ConfigInterface]]]:
        return [("flows", DemoSubDao)]


class DemoSubDao(ConfigInterface):
    def __init__(self):
        self.value = 1


class ResponseInfo(ConfigInterface):
    def __init__(self):
        self.status_code = 200
        self.reason = "ok"
        self.text = ""


if __name__ == "__main__":
    pass
