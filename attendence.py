import sys


if len(sys.argv) != 3 or sys.argv[1].strip() == "" or sys.argv[2].strip() == "":
    classes = 40       
    attended = 32     
    print("No input given – using default values.")
else:
    classes = int(sys.argv[1])
    attended = int(sys.argv[2])
    print("User provided values.")

attendance_percentage = (attended / classes) * 100

print("\n--- Attendance Report ---")
print("Total Classes Held:", total_classes)
print("Classes Attended:", attended_classes)
print(f"Attendance Percentage: {attendance_percentage:.2f}%")


if attendance_percentage < 75:
    print("Warning: Attendance below 75%")
else:
    print("Attendance is satisfactory.")
