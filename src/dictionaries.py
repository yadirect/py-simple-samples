
monthConversionsStr = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


print(monthConversionsStr["Nov"])
print(monthConversionsStr["Mar"])

print(monthConversionsStr.get("Dec"))

print(monthConversionsStr.get("Luv"))
print(monthConversionsStr.get("Luv", "Not a valid Key"))


monthConversionsInt = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December",
}


print(monthConversionsInt.get(7, "Not a valid Key"))
print(monthConversionsInt.get(12, "Not a valid Key"))
