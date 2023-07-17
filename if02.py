def main(a,b,c):
    if a<b and a<c:
        return a
    if b<a and b<c:
        return b
    if c<a and c<b:
        return c
print(main(2,9,7))
"""
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """