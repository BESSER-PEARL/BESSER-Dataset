





import java.util.List;
import java.util.ArrayList;

public class bibTeX_IsbnField  {

    private String isbn;





    private bibTeX_Book bibtex_book;


    public bibTeX_IsbnField(
        String isbn    ) {
        this.isbn = isbn;
    }


    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public bibTeX_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibTeX_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }

}