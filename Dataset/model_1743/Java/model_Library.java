





import java.util.List;
import java.util.ArrayList;

public class model_Library  {






    private model_Book model_book;




    private List<model_Book> model_books;


    public model_Library(
    ) {
        this.model_books = new ArrayList<>();
    }

    public model_Library(
        ArrayList<model_Book> model_books    ) {
        this.model_books = model_books;
    }


    public model_Book getModel_book() {
        return model_book;
    }

    public void setModel_book(model_Book model_book) {
        this.model_book = model_book;
    }
    public List<model_Book> getModel_books() {
        return model_books;
    }

    public void addModel_book(Model_book model_book) {
        this.model_books.add(model_book);
    }

}