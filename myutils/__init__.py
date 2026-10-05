def double_numbers(nums: list[int]) -> list[int]:
    return [n * 2 for n in nums]

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"