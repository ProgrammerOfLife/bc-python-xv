import unittest
from Note_Application import NotesApplication

class NotesApplicationTest(unittest.TestCase):
    def testAuthor(self):
        New_Note = NotesApplication("AuthorName")
        self.assertEqual("AuthorName", New_Note.author)
    def testList(self):
        New_Note = NotesApplication("Owner")
        self.assertEqual([], New_Note.note_list)
    def testCreate(self):
        New_Note = NotesApplication("ProgrammerOfLife")
        note_id = New_Note.create("Programming By Grace Because Life Comes through His Grace")
        self.assertEqual("Programming By Grace Because Life Comes through His Grace", New_Note.note_list[note_id])
    def testDelete(self):
        New_Note = NotesApplication("Am a New author")
        Note = New_Note.create("This Note is to be deleted")
        self.assertNotEqual("This Note is to be deleted", New_Note.delete(Note))
    
if __name__== "__main__":
    unittest.main()
