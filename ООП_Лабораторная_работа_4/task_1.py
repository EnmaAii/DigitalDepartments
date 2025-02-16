class OperatingSystem:
    """
    Базовый класс для всех операционных систем.

    Атрибуты:
        name (str): название операционной системы.
        version (str): версия операционной системы.
        _kernel_version (str): версия ядра (инкапсулированный атрибут).
    """

    def __init__(self, name: str, version: str, kernel_version: str):
        """
        Инициализация новой операционной системы.

        Аргументы:
            name (str): название операционной системы.
            version (str): версия операционной системы.
            kernel_version (str): версия ядра.
        """
        self.name = name
        self.version = version
        self._kernel_version = kernel_version  # Инкапсулированный атрибут, так как версия ядра не должна изменяться напрямую

    def __str__(self) -> str:
        """Возвращает строковое представление операционной системы."""
        return f"{self.name} версии {self.version} с ядром {self._kernel_version}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление операционной системы."""
        return f"OperatingSystem(name={self.name}, version={self.version}, kernel_version={self._kernel_version})"

    def update_system(self) -> None:
        """Обновляет операционную систему."""
        pass

    def shutdown(self) -> None:
        """Выключает операционную систему."""
        pass

    def get_kernel_version(self) -> str:
        """Возвращает версию ядра."""
        return self._kernel_version

class Linux(OperatingSystem):
    """
    Дочерний класс для операционных систем семейства Linux.

    Атрибуты:
        distribution (str): дистрибутив Linux.
    """

    def __init__(self, name: str, version: str, kernel_version: str, distribution: str):
        """
        Инициализация новой операционной системы Linux.

        Аргументы:
            name (str): название операционной системы.
            version (str): версия операционной системы.
            kernel_version (str): версия ядра.
            distribution (str): дистрибутив Linux.
        """
        super().__init__(name, version, kernel_version)
        self.distribution = distribution

    def __str__(self) -> str:
        """Возвращает строковое представление операционной системы Linux."""
        return f"{super().__str__()}, дистрибутив {self.distribution}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление операционной системы Linux."""
        return f"Linux(name={self.name}, version={self.version}, kernel_version={self._kernel_version}, distribution={self.distribution})"

    def update_system(self) -> None:
        """
        Обновляет операционную систему Linux.

        Перегрузка метода update_system для учета особенностей обновления Linux,
        например, использования пакетного менеджера.
        """
        print(f"Обновление системы {self.name} с использованием пакетного менеджера...")

    def access_terminal(self) -> None:
        """Открывает терминал в Linux."""
        pass


class Windows(OperatingSystem):
    """
    Дочерний класс для операционных систем семейства Windows.

    Атрибуты:
        edition (str): тип Windows (например, Home, Pro).
    """

    def __init__(self, name: str, version: str, kernel_version: str, edition: str):
        """
        Инициализация новой операционной системы Windows.

        Аргументы:
            name (str): название операционной системы.
            version (str): версия операционной системы.
            kernel_version (str): версия ядра.
            edition (str): тип Windows.
        """
        super().__init__(name, version, kernel_version)
        self.edition = edition

    def __str__(self) -> str:
        """Возвращает строковое представление операционной системы Windows."""
        return f"{super().__str__()}, тип {self.edition}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление операционной системы Windows."""
        return f"Windows(name={self.name}, version={self.version}, kernel_version={self._kernel_version}, edition={self.edition})"

    def update_system(self) -> None:
        """
        Обновляет операционную систему Windows.

        Перегрузка метода update_system для учета особенностей обновления Windows,
        например, использования Windows Update.
        """
        # Пример: использование Windows Update для обновления системы
        print(f"Обновление системы {self.name} с использованием Windows Update...")

    def open_task_manager(self) -> None:
        """Открывает диспетчер задач в Windows."""
        pass

if __name__ == "__main__":
    # Write your solution here
    ubuntu = Linux(name="Ubuntu", version="20.04", kernel_version="5.4.0", distribution="Ubuntu")
    print(ubuntu)
    ubuntu.update_system()
    ubuntu.access_terminal()

    print()

    windows10 = Windows(name="Windows", version="10", kernel_version="10.0.19041", edition="Pro")
    print(windows10)
    windows10.update_system()
    windows10.open_task_manager()
    pass
