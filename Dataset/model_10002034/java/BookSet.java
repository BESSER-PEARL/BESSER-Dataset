





import java.util.List;
import java.util.ArrayList;

public class BookSet  {

    private int bookID;
    private String bookName;



    public BookSet(
        int bookID,        String bookName    ) {
        this.bookID = bookID;
        this.bookName = bookName;
    }


    public int getBookid() {
        return bookID;
    }

    public void setBookid(int bookID) {
        this.bookID = bookID;
    }
    public String getBookname() {
        return bookName;
    }

    public void setBookname(String bookName) {
        this.bookName = bookName;
    }


}