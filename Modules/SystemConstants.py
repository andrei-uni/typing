import re


class SystemConstants:
    REPEAT_REGEX = re.compile(r"((\w)\2{4,})")
    REPLACEMENTS = {"—": "-",
                    "–": "-",
                    "‒": "-",
                    "―": "-",
                    "Ⅰ": "I",
                    "Ⅱ": "II",
                    "Ⅲ": "III",
                    "Ⅳ": "IV",
                    "Ⅴ": "V",
                    "Ⅵ": "VI",
                    "Ⅶ": "VII",
                    "Ⅷ": "VIII",
                    "Ⅸ": "IX",
                    "Ⅹ": "X",
                    "Ⅺ": "XI",
                    "Ⅻ": "XII",
                    "Ⅼ": "L",
                    "Ⅽ": "C",
                    "Ⅾ": "D",
                    "Ⅿ": "M",
                    }