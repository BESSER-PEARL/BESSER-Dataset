





import java.util.List;
import java.util.ArrayList;

public class book_Splash extends Page {

    private int duration;





    private book_Book book_book;


    public book_Splash(
        int duration    ) {
        super(
        );
        this.duration = duration;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(book_Book book_book) {
        this.book_book = book_book;
    }

}