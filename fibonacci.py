"""计算斐波那契数列。"""


def fibonacci(n: int) -> int:
    """返回第 n 个斐波那契数（从 0 开始：F(0)=0, F(1)=1）。"""
    if n < 0:
        raise ValueError("n 必须是非负整数")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"F({n}) = {fibonacci(n)}")
