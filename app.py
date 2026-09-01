"""Print a short student info card."""

STUDENT_INFO = {
    "Name": "Hamid Kabia",
    "Major": "Computer Science",
    "Interest": "Machine Learning and Cloud Development",
    "Skill to develop": "System Hardening",
}


def main():
    for label, value in STUDENT_INFO.items():
        print(f"{label}: {value}")


if __name__ == "__main__":
    main()
