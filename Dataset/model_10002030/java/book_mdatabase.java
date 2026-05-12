





import java.util.List;
import java.util.ArrayList;

public class book_mdatabase  {

    private String update;
    private String bookid;
    private String author;
    private String booktitle;





    private library library;


    public book_mdatabase(
        String update,        String bookid,        String author,        String booktitle    ) {
        this.update = update;
        this.bookid = bookid;
        this.author = author;
        this.booktitle = booktitle;
    }


    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }
    public String getBookid() {
        return bookid;
    }

    public void setBookid(String bookid) {
        this.bookid = bookid;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }

    public library getLibrary() {
        return library;
    }

    public void setLibrary(library library) {
        this.library = library;
    }

}