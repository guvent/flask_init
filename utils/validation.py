class Validation:
    payload = None

    def __init__(self, payload):
        self.payload = payload

    def validate_dict(self, validate_rules):
        if self.payload is not None:
            if type(self.payload) is dict:
                field_name_list = dict(self.payload).keys()

                if type(validate_rules) is dict:
                    for field_name in field_name_list:
                        if str(field_name) in dict(validate_rules).keys():
                            rules = validate_rules[str(field_name)]
                            if type(rules) is not dict:
                                rules["type"] = str(rules["type"]) if "type" in dict(rules).keys() else None
                                return False, {
                                    "message": "Invalid Rules!",
                                    "code": 110,
                                    "field": str(field_name),
                                    "rules": rules
                                }

                            if self.payload[str(field_name)] is None and rules["required"] is False:
                                self.payload[str(field_name)] = rules["default"] if "default" in rules else None

                            else:
                                if type(self.payload[str(field_name)]) is not rules["type"]:
                                    if type(rules["type"]) is type:
                                        rules["type"] = rules["type"].__name__
                                    else:
                                        str(rules["type"])

                                    return False, {
                                        "message": "Invalid Field Type!",
                                        "code": 102,
                                        "field": str(field_name),
                                        "rules": rules
                                    }

                                if rules["type"] is str:
                                    if len(str(self.payload[str(field_name)])) < int(rules["min"]):
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Invalid Field Value!",
                                            "code": 101,
                                            "field": str(field_name),
                                            "rules": rules
                                        }
                                    if len(str(self.payload[str(field_name)])) > int(rules["max"]):
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Invalid Field Value!",
                                            "code": 101,
                                            "field": str(field_name),
                                            "rules": rules
                                        }
                                    if str(self.payload[str(field_name)]).strip() == "" and rules["required"]:
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Field Value Required!",
                                            "code": 102,
                                            "field": str(field_name),
                                            "rules": rules
                                        }

                                if rules["type"] is int:
                                    if int(self.payload[str(field_name)]) < int(rules["min"]):
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Invalid Field Value!",
                                            "code": 101,
                                            "field": str(field_name),
                                            "rules": rules
                                        }
                                    if int(self.payload[str(field_name)]) > int(rules["max"]):
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Invalid Field Value!",
                                            "code": 101,
                                            "field": str(field_name),
                                            "rules": rules
                                        }

                                if rules["type"] is float:
                                    if float(self.payload[str(field_name)]) < float(rules["min"]):
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Invalid Field Value!",
                                            "code": 101,
                                            "field": str(field_name),
                                            "rules": rules
                                        }
                                    if float(self.payload[str(field_name)]) > float(rules["max"]):
                                        if type(rules["type"]) is type:
                                            rules["type"] = rules["type"].__name__
                                        else:
                                            str(rules["type"])

                                        return False, {
                                            "message": "Invalid Field Value!",
                                            "code": 101,
                                            "field": str(field_name),
                                            "rules": rules
                                        }

                        else:
                            return False, {
                                "message": "Parameter Required!",
                                "code": 100,
                                "field": str(field_name),
                                "rules": None
                            }

                    for field_rule_name in dict(validate_rules).keys():
                        if field_rule_name not in field_name_list:
                            rules = validate_rules[str(field_rule_name)]
                            if type(rules) is not dict:
                                rules["type"] = str(rules["type"]) if "type" in dict(rules).keys() else None
                                return False, {
                                    "message": "Invalid Rules!",
                                    "code": 110,
                                    "field": str(field_rule_name),
                                    "rules": rules
                                }

                            if "required" in dict(rules).keys():
                                if rules["required"] is True:
                                    return False, {
                                        "message": "Parameter Required!",
                                        "code": 100,
                                        "field": str(field_rule_name),
                                        "rules": None
                                    }

                            if "default" in dict(rules).keys():
                                self.payload[str(field_rule_name)] = rules["default"]
                            else:
                                self.payload[str(field_rule_name)] = None

                    return True, None

                return False, {
                    "message": "Invalid Parameters!",
                    "code": 111,
                    "field": None,
                    "rules": None
                }

        return False, {
            "message": "Invalid Payload!",
            "code": 120,
            "field": None,
            "rules": None
        }
