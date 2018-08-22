from .models import JobNote
from datetime import datetime

def unfuck_dates():
    for jobnote in JobNote.objects.all():
        try:
            jobnote.note_date = datetime.date(jobnote.note_date)

        except Exception as e:
            print(e) 
            jobnote.note_date = datetime.today()
        finally:
            jobnote.save()