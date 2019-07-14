[Return to main page](README.md)

------

<a name="VariableTextFormat"></a>

These are the different formatting codes used for Variable Text in LightBurn.

#### Date / Time text format

When using the Date/Time mode for text, the system will automatically substitute special combinations of characters with values for the current local date and time.

For example, if your text field is "d/MM/yyyy" the system would replace it with "15/6/2019". The values you can use for substitution are listed below.

These expressions may be used for the date:

| Output                                                       | Expression |
| ------------------------------------------------------------ | ---------- |
| the day as number without a leading zero (1 to 31)           | d          |
| the day as number with a leading zero (01 to 31)             | dd         |
| the abbreviated localized day name (e.g. 'Mon' to 'Sun'). Uses the system locale to localize the name. | ddd        |
| the long localized day name (e.g. 'Monday' to 'Sunday'). Uses the system locale to localize the name. | dddd       |
| the month as number without a leading zero (1-12)            | M          |
| the month as number with a leading zero (01-12)              | MM         |
| the abbreviated localized month name (e.g. 'Jan' to 'Dec'). Uses the system locale to localize the name. | MMM        |
| the long localized month name (e.g. 'January' to 'December'). Uses the system locale to localize the name. | MMMM       |
| the year as two digit number (00-99)                         | yy         |
| the year as four digit number                                | yyyy       |

These expressions may be used for the time:

| Expression | Output                                                       |
| ---------- | ------------------------------------------------------------ |
| h          | the hour without a leading zero (0 to 23 or 1 to 12 if AM/PM display) |
| hh         | the hour with a leading zero (00 to 23 or 01 to 12 if AM/PM display) |
| H          | the hour without a leading zero (0 to 23, even with AM/PM display) |
| HH         | the hour with a leading zero (00 to 23, even with AM/PM display) |
| m          | the minute without a leading zero (0 to 59)                  |
| mm         | the minute with a leading zero (00 to 59)                    |
| s          | the whole second without a leading zero (0 to 59)            |
| ss         | the whole second with a leading zero where applicable (00 to 59) |
| z          | the fractional part of the second, to go after a decimal point, without trailing zeroes (0 to 999). Thus "`s.z`" reports the seconds to full available (millisecond) precision without trailing zeroes. |
| zzz        | the fractional part of the second, to millisecond precision, including trailing zeroes where applicable (000 to 999). |
| AP or A    | use AM/PM display. *A/AP* will be replaced by either "AM" or "PM". |
| ap or a    | use am/pm display. *a/ap* will be replaced by either "am" or "pm". |
| t          | the time zone (for example "CEST")                           |

Any sequence of characters enclosed in single quotes will be included verbatim in the output string (stripped of the quotes), even if it contains formatting characters. Two consecutive single quotes ('') are replaced by a single quote in the output. All other characters in the input string are included verbatim in the output string.

Formats without separators (e.g. "ddMM") are supported but must be used with care, as the resulting strings aren't always reliably readable (e.g. if "dM" produces "212" it could mean either the 2nd of December or the 21st of February).

Example format strings (for the date & time 21 May 2001 14:13:09.120):

| Input         | Result        |
| ------------- | ------------- |
| dd.MM.yyyy    | 21.05.2001    |
| ddd MMMM d yy | Tue May 21 01 |
| hh:mm:ss.zzz  | 14:13:09.120  |
| hh:mm:ss.z    | 14:13:09.12   |
| h​ : m : s ap  | 2 : 13 : 9 pm |



#### Serial number text format

When using the Serial mode for text, the system will automatically substitute certain special combinations of characters with the current serial number value, and other characters control how it is formatted.

These expressions may be used for serial numbers:

| Output                                               | Expression |
| ---------------------------------------------------- | ---------- |
| The serial number as a decimal value                 | d          |
| The serial number as a hexadecimal value, lower case | h          |
| The serial number as a hexadecimal value, upper case | H          |
| Tells LightBurn to pad the number with leading zeros | 0          |

The number of characters used controls how many digits the system will display.  If the serial number is larger than the number of digits allowed, as many digits as will fit from the end of the number will be displayed.  For example, if your serial number is 1234, the table below shows how that number would be formatted for each of the displayed formatting inputs:

| Input  | Output | Input   | Output |
| ------ | ------ | ------- | ------ |
| d      | 4      | 0d      | 4      |
| dd     | 34     | 0dd     | 34     |
| ddd    | 234    | 0ddd    | 234    |
| dddd   | 1234   | 0dddd   | 1234   |
| ddddd  | 1234   | 0ddddd  | 01234  |
| dddddd | 1234   | 0dddddd | 001234 |

You cannot mix decimal and hexadecimal formatting in the same text entry, and you cannot split a serial number with other characters.  For example, this string is not valid: ddd-ddd because of the hyphen between the two groups of format characters.

Like the Date / Time formatting, any text between a pair of single quotes is copied exactly to the output, and a pair of single quotes together is replaced by one single quote in the output.



#### CSV/Merge text format

When using the CSV/Merge mode for text, the system will automatically substitute certain special combinations of characters with entries from the selected row of a CSV file. A CSV file is "Comma Separated Values" - a very simple text format that uses a line in the file as the row, and commas to separate columns in the file.

For example:

```
LightBurn,80,10
Corel,300,20
```

In a CSV/Merge entry in LightBurn, the text you enter uses the percent sign followed by a number to look up a column in the current row of the CSV file. For example, using this text with the above table:

​	I'm thinking of buying %0 - it costs $%1

Would display:

​	I'm thinking of buying LightBurn - it costs $80

Columns are numbered starting from 0.



#### Cut Setting text format

When using the Cut Setting mode for text, the system will automatically substitute certain characters with values from the cut setting applied to the text.

Like the Date / Time or Serial number formatting, any text between a pair of single quotes is copied exactly to the output, and a pair of single quotes together is replaced by one single quote in the output.

| Expression | Output                                                   |
| ---------- | -------------------------------------------------------- |
| s          | speed, as a number in the current speed units            |
| S          | speed, including the current units (like mm/sec)         |
| p          | max power, as a percentage                               |
| P          | max power, including the percent sign                    |
| m          | min power, as a percentage                               |
| M          | min power, including the percent sign                    |
| d          | DPI, as a number, always dots per inch                   |
| i          | interval, in the current distance units                  |
| I          | interval, including the current distance units (like mm) |

