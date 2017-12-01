from os.path import isfile
import pickle


class SchoolDB:
    def __init__(self, schoolinitializer):

        self.schoolinitializer = schoolinitializer
        self.file_name = r".\enroll.dat"
        self.data = schoolinitializer.enrollments

        self.load_data()

    def load_data(self):

        if (isfile(self.file_name)):
            self.file = open(self.file_name, 'rb')
            self.enrollments = pickle.load(self.file)
            self.file.close()
        else:
            self.enrollments = self.schoolinitializer.enrollments

    def save_data(self):

        self.file = open(self.file_name, 'wb')
        pickle.dump(self.enrollments, self.file)
        self.file.close()
