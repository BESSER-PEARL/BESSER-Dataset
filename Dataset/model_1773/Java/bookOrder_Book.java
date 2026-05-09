





import java.util.List;
import java.util.ArrayList;

public class bookOrder_Book  {

    private String title;





    private bookOrder_BookOrder bookorder_bookorder;


    public bookOrder_Book(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bookOrder_BookOrder getBookorder_bookorder() {
        return bookorder_bookorder;
    }

    public void setBookorder_bookorder(bookOrder_BookOrder bookorder_bookorder) {
        this.bookorder_bookorder = bookorder_bookorder;
    }

}