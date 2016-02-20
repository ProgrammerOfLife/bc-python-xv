class NotesApplication(object):
    note_layout = "Note ID: {} \n{} \n\nBy Author {}\n"
    def __init__(self, author):
        self.author = author
        self.note_list = []
    def create(self, note_content):
        self.note_list.append(note_content)
        return (len(self.note_list) - 1)
    def list_all(self):
        content = ""
        for i in range(len(self.note_list)):
            content += self.note_layout.format(i, self.note_list[i], self.author)
        return content
    def get(self, note_id):
        #check valid id
        return self.note_list[note_id]
    def search(self, search_text):
        content = "Showing results for search "+search_text+"\n"
        found = 0
        for i in range(len(self.note_list)):
            if self.note_list[i].find(search_text) > -1:
                content += self.note_layout.format(i, self.note_list[i], self.author)
                found += 1
        if found == 0:
            return "No Result found"
        return content
    def delete(self, note_id):
        del(self.note_list[note_id])
        return self
    def edit(self, note_id, new_note):
        self.note_list[note_id] = new_note
        return self

