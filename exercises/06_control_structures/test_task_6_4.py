def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_6_4

    out, err = capsys.readouterr()
    correct_stdout = "['cfg_01.txt', 'cfg_04.txt', 'cfg_08.txt', 'cfg_09.txt', 'cfg_12.txt', 'cfg_15.txt']"
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_6_4

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_6_4) if not var.startswith("_")]

    correct_result = [
        "cfg_01.txt",
        "cfg_04.txt",
        "cfg_08.txt",
        "cfg_09.txt",
        "cfg_12.txt",
        "cfg_15.txt",
    ]

    assert (
        "result" in task_vars
    ), "Список має бути записаний у змінну result"
    assert (
        type(task_6_4.result) == list
    ), f"За завданням у змінній result має бути список, а в ній {type(task_6_4.result).__name__}"
    assert (
        correct_result == task_6_4.result
    ), f"У змінній result має бути список {correct_result}"
