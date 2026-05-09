





import java.util.List;
import java.util.ArrayList;

public class books_Book  {

    private String title;
    private int pages;
    private String isbn;





    private books_Catalog books_catalog;


    public books_Book(
        String title,        int pages,        String isbn    ) {
        this.title = title;
        this.pages = pages;
        this.isbn = isbn;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public books_Catalog getBooks_catalog() {
        return books_catalog;
    }

    public void setBooks_catalog(books_Catalog books_catalog) {
        this.books_catalog = books_catalog;
    }

}