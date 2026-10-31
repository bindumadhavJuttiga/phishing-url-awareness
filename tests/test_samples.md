
# Test Results

Python version used: Python 3.13
Operating system: Windows 11
Date: 30-10-2026

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | IP address + HTTP warnings detected | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | @ symbol + HTTP warnings detected | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Many hostname segments detected | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Punycode-style hostname detected | PASS |

## Notes

I learned how to identify suspicious URL characteristics using Python.
I understood how URL parsing, regular expressions and conditional statements work.
I also learned that no warning signs found does not guarantee that a URL is safe.
