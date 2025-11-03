import random
from classrooms.models import FreeClass

def run():
    blocks = ['36 ', '37 ', '38 ', '39 ']  # Block numbers
    floors = ['1 Floor', '2 Floor', '3 Floor', '4 Floor', '5 Floor', '6 Floor', '7 Floor']  # No Ground Floor

    count = 0
    for block in blocks:
        for floor in floors:
            # Extract floor number (1 to 7)
            floor_num = int(floor.split()[0])

            for room_suffix in range(1, 8):  # Rooms 101 to 107, etc.
                room_no = f"{floor_num}{str(room_suffix).zfill(2)}"  # Example: 101, 102, 201, etc.

                for day, _ in FreeClass.DAY_CHOICES:
                    for time, _ in FreeClass.TIME_CHOICES:
                        room_type = random.choice([t[0] for t in FreeClass.TYPE_CHOICE])
                        room_status = random.choice([s[0] for s in FreeClass.STATUS_CHOICE])
                        is_occupied = room_status == 'Occupied'

                        FreeClass.objects.update_or_create(
                            Block=block,
                            Day=day,
                            Time=time,
                            Floor=floor,
                            Room_No=room_no,
                            defaults={
                                'Room_Status': room_status,
                                'Room_Type': room_type,
                                'is_occupied': is_occupied
                            }
                        )
                        count += 1

    print(f"✅ Successfully added/updated {count} FreeClass entries!")
