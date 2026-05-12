





import java.util.List;
import java.util.ArrayList;

public class BookSet  {

    private int bookIsbn;
    private String bookTitle;





    private Search search;


    public BookSet(
        int bookIsbn,        String bookTitle    ) {
        this.bookIsbn = bookIsbn;
        this.bookTitle = bookTitle;
    }


    public int getBookisbn() {
        return bookIsbn;
    }

    public void setBookisbn(int bookIsbn) {
        this.bookIsbn = bookIsbn;
    }
    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }

    public Search getSearch() {
        return search;
    }

    public void setSearch(Search search) {
        this.search = search;
    }

}