import re


class SystemConstants:
    REPEAT_REGEX = re.compile(r"((\w)\2{5,})")
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
    KeyboardSymbols = " ёЁ1!23№4;5%6:7?8*9(0)-_=+йЙцЦуУкКеЕнНгГшШщЩзЗхХъЪ\/фФыЫвВаАпПрРоОлЛдДжЖэЭяЯчЧсСмМиИтТьЬбБюЮ.,~`@#$%^&|qQwWeErRtTyYuUiIoOpP[{]}aAsSdDfFgGhHjJkKlL:'\"zZxXcCvVbBnNmM<>"