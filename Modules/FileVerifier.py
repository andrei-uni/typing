from Modules.SystemConstants import SystemConstants


class FileVerifier:
    @staticmethod
    def replace_not_keyboard_symbols(text):
        new_text = ""
        for index in range(len(text)):
            if text[index] in SystemConstants.REPLACEMENTS.keys():
                new_text += SystemConstants.REPLACEMENTS[text[index]]
            else:
                new_text += text[index]
        return new_text

    @staticmethod
    def check_not_keyboard_symbols(text):
        for index in range(len(text)):
            if text[index] not in SystemConstants.KeyboardSymbols:
                return True
        return False
