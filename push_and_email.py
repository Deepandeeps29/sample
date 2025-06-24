import subprocess
import os

print("📦 Staging files...")
os.system("git add .")

print("📝 Committing changes...")
os.system('git commit -m "Auto commit from script"')

print("🚀 Pushing to GitHub...")
os.system("git push")

print("📧 Sending report...")
os.system("python send_email.py")
