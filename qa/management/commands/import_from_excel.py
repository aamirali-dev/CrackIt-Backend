from django.core.management.base import BaseCommand
import pandas as pd
from pathlib import Path
from qa.models import QuestionCategory, Question, Solution

class Command(BaseCommand):
    help = 'Populates the database with data from excel files. sheet name goes to categories, first column goes to questions, second column goes to answers' 

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="+", type=str)


    def handle(self, *args, **options):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        for filename in options['files']:
            print(BASE_DIR / filename)
            xl = pd.ExcelFile(filename)
            for sheet in xl.sheet_names:
                category = QuestionCategory(name=sheet)
                category.save()
                data = xl.parse(sheet)
                for q in data.iloc[:,0]:
                    qu = Question(category=category, description=q)
                    qu.save()