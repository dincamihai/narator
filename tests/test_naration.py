from narator import narator


def test_narate_single_topic():
    comments = [
        str(
            "Title 1\n"
            "todo create PR\n"
            "done investigated\n"
            "done discussed with team#1"
        )
    ]
    output = narator.aggregate(comments)
    assert output.decode('utf8') == str(
        "#### Title 1\n"
        "  - DONE:\n"
        "    - investigated\n"
        "    - discussed with team#1\n"
        "  - TODO:\n"
        "    - create PR"
    )


def test_narate_two_topics():
    comments = [
        str(
            "Topic 1\n"
            "todo create PR\n"
            "done discussed with team#1\n"
        ),
        str(
            "Topic 2\n"
            "done task#1\n"
            "todo task#2\n"
        )
    ]
    output = narator.aggregate(comments)
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


def test_narate_two_topics_with_one_title():
    comments = [
        str(
            "Great title for topic#1\n"
            "todo create PR"
        ),
        str(
            "Topic 2\n"
            "done task#1\n"
        ),
    ]
    output = narator.aggregate(comments)
    assert output.decode('utf8') == str(
        "#### Great title for topic#1\n"
        "  - TODO:\n"
        "    - create PR\n\n"
        "#### Topic 2\n"
        "  - DONE:\n"
        "    - task#1"
    )


def test_narate_multiline_comment():
    comments = [
        str(
            "Title for topic#1\r\n"
            "done investigated\r\n"
            "done discussed with team#1\n"
            "todo create PR\n")
    ]
    output = narator.aggregate(comments)
    assert output.decode('utf8') == str(
        "#### Title for topic#1\n"
        "  - DONE:\n"
        "    - investigated\n"
        "    - discussed with team#1\n"
        "  - TODO:\n"
        "    - create PR"
    )
