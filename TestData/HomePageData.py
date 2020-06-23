import openpyxl


class HomePageData:
    test_HomePage_data = [{"first_name": "Sergey", "last_name": "Akhmerov", "gender": "Male"},
                          {"first_name": "Rahul", "last_name": "Shetty", "gender": "Male"}]

    @staticmethod
    def getTestData(test_case_name):
        book = openpyxl.load_workbook("/Users/sergeyakhmerov/Desktop/PythonDemo.xlsx")
        sheet = book.active
        Dict = {}
        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, column=1).value == test_case_name:
                for j in range(2, sheet.max_column + 1):
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

        return[Dict]