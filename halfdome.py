from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

# === Customize these if you want ===
hike_date = "Sunday, March 22, 2026"
meeting_time = "6:00 AM sharp"
meeting_point = "Happy Isles Trailhead, Yosemite Valley"
hike_details = (
    "• ~16–17 miles round trip\n"
    "• ~4,800–5,300 ft elevation gain\n"
    "• Expect 10–14 hours total (strenuous!)\n"
    "• Iconic cables section — gloves recommended\n"
    "• Bring: plenty of water (4L+), snacks, layers, headlamp, permit"
)
inviter = "Suman"
invitees = ["Vatsalya", "Mohit"]

# === Create the PDF ===
filename = "Half_Dome_Hike_Invitation.pdf"
c = canvas.Canvas(filename, pagesize=A4)
width, height = A4  # in points (~595 × 842)

# Background color tint (light)
c.setFillColorRGB(0.96, 0.98, 1.0)
c.rect(0, 0, width, height, fill=1)

# Title
c.setFillColor(colors.darkblue)
c.setFont("Helvetica-Bold", 36)
c.drawCentredString(width/2, height - 1.2*inch, "You're Invited!")

# Subtitle / Event name
c.setFont("Helvetica-Bold", 24)
c.drawCentredString(width/2, height - 2.0*inch, "Half Dome Summit Hike")

# Date & details block
c.setFillColor(colors.black)
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(width/2, height - 3.0*inch, hike_date)

c.setFont("Helvetica", 14)
y = height - 3.8*inch
c.drawCentredString(width/2, y, f"Meet at {meeting_time} | {meeting_point}")
y -= 0.4*inch
c.drawCentredString(width/2, y, "Yosemite National Park – California")

# Main body text
c.setFont("Helvetica", 13)
y -= 0.8*inch
text = c.beginText(1.2*inch, y)
text.setLeading(18)
text.textLines(
    "Dear Vatsalya & Mohit,\n\n"
    "Join me for an epic adventure to conquer Half Dome!\n"
    "This is one of the most iconic and rewarding hikes in the world —\n"
    "waterfalls, granite domes, epic views, and the famous final cables.\n\n"
    "Get ready for a big day — early start, strong legs, and great company.\n\n"
    f"Hope you both can make it!\n\n"
    "Details:\n" + hike_details + "\n\n"
    "Reply soon — spots (and motivation) are limited!\n\n"
    "See you on the trail,\n"
)
text.textLine("")
text.setFont("Helvetica-Oblique", 14)
text.textLine(f"— {inviter}")
c.drawText(text)

# Footer / note
c.setFont("Helvetica-Oblique", 10)
c.setFillColorRGB(0.4, 0.4, 0.4)
c.drawCentredString(width/2, 0.8*inch,
    "Permits required — please confirm you have / are applying for a valid Half Dome permit")

# Decorative line
c.setStrokeColor(colors.darkblue)
c.setLineWidth(2)
c.line(1.5*inch, height - 2.7*inch, width - 1.5*inch, height - 2.7*inch)

c.showPage()
c.save()

print(f"PDF created: {filename}")
