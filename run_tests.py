import subprocess
import sys
import os

if __name__ == "__main__":
    # Устанавливаем корень проекта в PYTHONPATH
    os.environ["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))

    # Формируем команду запуска pytest с coverage
    pytest_cmd = [
        sys.executable, "-m", "pytest",
        "tests",                     # папка с тестами
        "--cov=.",                    # покрытие всего проекта
        "--cov-report=term-missing",  # показать пропущенные строки
        "--cov-report=html",          # создать HTML отчет
        "-q"                          # краткий вывод
    ]

    # Запуск pytest
    result = subprocess.run(pytest_cmd)

    # Финальный вывод
    print("\n" + "="*60)
    if result.returncode == 0:
        print("✅ Все тесты прошли успешно!")
    else:
        print("❌ Есть ошибки при выполнении тестов!")
    print("HTML-отчет с покрытием создан в папке 'htmlcov/'")
    print("="*60 + "\n")

    # Выход с кодом завершения pytest
    sys.exit(result.returncode)
