import re
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import count_calls


@count_calls
def monkey_input_r2(prompt):
    __tracebackhide__ = True
    if monkey_input_r2.total_calls == 1:
        return "r2"
    elif monkey_input_r2.total_calls == 2:
        # при запросе параметры должны указываться доступные значения для
        # устройства. Для r2: "location, vendor, model, ios, ip"
        if re.search(r"location.+vendor.+model.+ios.+ip", prompt):
            return "ip"
        else:
            pytest.fail(
                "В запросе параметра не указаны доступные значения для устройства. "
                "Для r2 это такие значения "
                "(location, vendor, model, ios, ip)"
            )


@count_calls
def monkey_input_sw1(prompt):
    __tracebackhide__ = True
    if monkey_input_sw1.total_calls == 1:
        return "sw1"
    elif monkey_input_sw1.total_calls == 2:
        if re.search(r"location.+vendor.+model.+ios.+ip.+vlans.+routing", prompt):
            return "ios"
        else:
            pytest.fail(
                "В запросе параметра не указаны доступные значения для устройства. "
                "Для sw1 это такие значения "
                "(location, vendor, model, ios, ip, vlans, routing)"
            )


def test_task_r2(capsys, monkeypatch):
    """
    Перевірка роботи завдання при вводе r2
    """
    monkeypatch.setattr("builtins.input", monkey_input_r2)
    import task_5_3b

    out, err = capsys.readouterr()
    correct_stdout = "10.255.0.2"

    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_sw1(capsys, monkeypatch):
    """
    Перевірка роботи завдання при вводе sw1
    """
    monkeypatch.setattr("builtins.input", monkey_input_sw1)
    if sys.modules.get("task_5_3b"):
        del sys.modules["task_5_3b"]
    import task_5_3b

    out, err = capsys.readouterr()
    correct_stdout = "3.6.XE"
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
