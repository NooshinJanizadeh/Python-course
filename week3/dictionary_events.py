events = {
    "Night of Museums": "19.09.2026",
    "Dortmund Music Festival": "19.09.2026",
    "Art Exhibition": "20.09.2026",
    "Tech Conference": "19.09.2026",
    "Food Festival": "18.09.2026",
    "Theater Night": "19.09.2026"
}

print("Events running during the Night of Museums on 19.09.2026:")
for event, date in events.items():
    if date == "19.09.2026":
        print("-", event)