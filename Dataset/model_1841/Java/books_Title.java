





import java.util.List;
import java.util.ArrayList;

public class books_Title  {

    private String lan;
    private String text;





    private books_Book books_book;


    public books_Title(
        String lan,        String text    ) {
        this.lan = lan;
        this.text = text;
    }


    public String getLan() {
        return lan;
    }

    public void setLan(String lan) {
        this.lan = lan;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public books_Book getBooks_book() {
        return books_book;
    }

    public void setBooks_book(books_Book books_book) {
        this.books_book = books_book;
    }

}