





import java.util.List;
import java.util.ArrayList;

public class SearchRequest  {






    private book book;




    private Catalog catalog;


    public SearchRequest(
    ) {
    }



    public book getBook() {
        return book;
    }

    public void setBook(book book) {
        this.book = book;
    }
    public Catalog getCatalog() {
        return catalog;
    }

    public void setCatalog(Catalog catalog) {
        this.catalog = catalog;
    }

}