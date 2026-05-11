




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_Note  {

    private String id;
    private String content;
    private String noteAuthor;
    private LocalDate date;





    private lobj_Sharednotes lobj_sharednotes;


    public lobj_Note(
        String id,        String content,        String noteAuthor,        LocalDate date    ) {
        this.id = id;
        this.content = content;
        this.noteAuthor = noteAuthor;
        this.date = date;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getNoteauthor() {
        return noteAuthor;
    }

    public void setNoteauthor(String noteAuthor) {
        this.noteAuthor = noteAuthor;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public lobj_Sharednotes getLobj_sharednotes() {
        return lobj_sharednotes;
    }

    public void setLobj_sharednotes(lobj_Sharednotes lobj_sharednotes) {
        this.lobj_sharednotes = lobj_sharednotes;
    }

}