import os

PART_A = "I can sense my toast is exactly 3 seconds from burning, but only while I'm in the shower, "
PART_B = "12 steps away from the kitchen."

ENTRY = PART_A + PART_B

EXPECTED = "I can sense my toast is exactly 3 seconds from burning, but only while I'm in the shower, 12 steps away from the kitchen."

assert ENTRY == EXPECTED, "joined entry does not match expected text"
assert 1 <= len(ENTRY) <= 140, "entry length out of bounds"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
