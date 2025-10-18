#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
year = form.getvalue('year')
from datetime import date, datetime, timedelta

def calculate_easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    return datetime.date(year=year, month=n, day=p)

def format_date(easter_date, format_type):
    day = easter_date.strftime("%d")
    suffix = "th" if 11 <= int(day) <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(int(day) % 10, 'th')
    if format_type == 'numeric':
        return easter_date.strftime(f"%d/%m/%Y")
    elif format_type == 'verbose':
        return f"{day}{suffix} {easter_date.strftime('%B %Y')}"
    else:
        numeric_format = easter_date.strftime("%d/%m/%Y")
        verbose_format = f"{day}{suffix} {easter_date.strftime('%B %Y')}"
        return f"{numeric_format} and {verbose_format}"

if year and year.isdigit():
    year = int(year)
    format_type = form.getvalue('format')

    easter_date = calculate_easter_date(year)
    formatted_date = format_date(easter_date, format_type)

    print(f"Content-type: text/html\n\n<html><head><title>Easter Date Result</title></head><body><h2>Easter Date:</h2><p>{formatted_date}</p></body></html>")
else:
    print("Content-type: text/html\n\n<html><head><title>Error</title></head><body><h2>Error:</h2><p>Please provide a valid year.</p></body></html>")
