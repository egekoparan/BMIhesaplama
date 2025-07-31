class InvalidHeightError(Exception):
    def __init__(self, message="Geçersiz boy değeri. Lütfen pozitif bir sayı girin."):
        super().__init__(message)

class InvalidWeightError(Exception):
    def __init__(self, message="Geçersiz kilo değeri. Lütfen pozitif bir sayı girin."):
        super().__init__(message)

class EmptyInputError(Exception):
    def __init__(self, message="Giriş alanları boş bırakılamaz."):
        super().__init__(message)
