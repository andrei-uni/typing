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