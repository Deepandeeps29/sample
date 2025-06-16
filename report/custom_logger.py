from datetime import datetime
import os

class CustomLogger:
    def __init__(self, file_path="report/log.html"):
        self.file_path = file_path
        self.is_new_file = not os.path.exists(file_path)

        # Create the report directory if not exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # mode = "w" if self.is_new_file else "a"
        # self.file = open(file_path, mode, encoding="utf-8")

        self.file = open(file_path, "a", encoding="utf-8")

        if self.is_new_file:
            self.file.write(f"""
<html>
<head>
    <title>Qspider Test Log</title>
    <style>
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .PASS {{ color: green; }}
        .FAIL {{ color: red; }}
        .INFO {{ color: blue; }}
    </style>
</head>
<body>
<h2>Qspider Test Log</h2>
<p>Start Time: {datetime.now()}</p>
""")

        # Always start a new test table
        self.file.write("<table><tr><th>Time</th><th>Step</th><th>Status</th><th>Details</th></tr>\n")

    def log(self, step, status="INFO", details=""):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file.write(f"<tr><td>{now}</td><td>{step}</td><td class='{status}'>{status}</td><td>{details}</td></tr>\n")

    def finalize(self):
        # End this test's table only (don’t close full HTML if appending again later)
        self.file.write("</table>\n")
        self.file.close()

    def close_html(self):
        # Optional: final closing tag after all tests are done
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write("</body></html>")
