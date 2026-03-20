class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # пропускаем не-буквенно-цифровые символы слева
            while left < right and not s[left].isalnum():
                left += 1

            # пропускаем не-буквенно-цифровые символы справа
            while left < right and not s[right].isalnum():
                right -= 1

            # если символы в нижнем регистре не совпадают — это не палиндром
            if s[left].lower() != s[right].lower():
                return False

            # сдвигаем указатели дальше
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    # создаем экземпляр класса Solution
    solution = Solution()

    # список с тестами в формате: (входная строка, ожидаемый результат)
    test_cases = [
        ("A man, a plan, a canal: Panama", True),  # Example 1
        ("race a car", False),  # Example 2
        (" ", True),  # Example 3
        ("0P", False)  # дополнительный тест с цифрами и буквами
    ]

    # запускаем цикл по всем тестам
    for i, (test_input, expected_output) in enumerate(test_cases, 1):
        # вызываем наш метод
        result = solution.isPalindrome(test_input)

        # проверяем, совпал ли результат с ожидаемым
        if result == expected_output:
            status = "ПРОЙДЕН"
        else:
            status = f"ОШИБКА (Получено: {result}, Ожидалось: {expected_output})"

        # выводим красивый отчет в консоль
        print(f"Тест {i}:")
        print(f"  Вход: s = \"{test_input}\"")
        print(f"  Выход: {result}")
        print(f"  Статус: {status}")
        print("-" * 30)
