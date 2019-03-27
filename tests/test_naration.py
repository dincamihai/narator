from narator import narator


def test_narate_single_topic():
    body = str(
        "Title 1\n"
        "todo create PR\n"
        "done investigated\n"
        "done discussed with team#1"
    )
    output = narator.aggregate(body)
    assert output.decode('utf8') == str(
        "#### Title 1\n"
        "  - DONE:\n"
        "    - investigated\n"
        "    - discussed with team#1\n"
        "  - TODO:\n"
        "    - create PR"
    )


def test_narate_two_topics():
    body = str(
        "Topic 1\n"
        "todo create PR\n"
        "done discussed with team#1\n"
        "Topic 2\n"
        "done task#1\n"
        "todo task#2\n"
    )
    output = narator.aggregate(body)
    assert output.decode('utf8') == str(
        "#### Topic 1\n"
        "  - DONE:\n"
        "    - discussed with team#1\n"
        "  - TODO:\n"
        "    - create PR\n\n"
        "#### Topic 2\n"
        "  - DONE:\n"
        "    - task#1\n"
        "  - TODO:\n"
        "    - task#2"
    )
