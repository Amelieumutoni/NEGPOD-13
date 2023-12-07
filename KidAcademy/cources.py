def display_course():
    course_title = "Rwandan Culture Course"
    course_description = "This course will provide an introduction to the Rwandan culture. You will learn about the customs, traditions, and values that shape Rwandan culture. You will also have the opportunity to practice the local language and learn about the unique geographical features of Rwanda."

    culture = {
        "name": "Rwanda",
        "customs": ["Respect for Elders", "Politeness", "Family is important"],
        "traditions": ["Umuganda", "Rural Housing", "Burial Traditions"],
        "geographical_features": ["Mountain ranges", "Lakes", "Forests"],
        "language": "Kinyarwanda",
        "image": "rwanda.jpg"
    }

    print("Course Title: " + course_title)
    print("Course Description: " + course_description)
    print("")
    print("Culture Name: " + culture["name"])
    print("Customs: ")
    for custom in culture["customs"]:
        print("- " + custom)
    print("Traditions: ")
    for tradition in culture["traditions"]:
        print("- " + tradition)
    print("Geographical Features: ")
    for feature in culture["geographical_features"]:
        print("- " + feature)
    print("Language: " + culture["language"])
    print("Image: " + culture["image"])


