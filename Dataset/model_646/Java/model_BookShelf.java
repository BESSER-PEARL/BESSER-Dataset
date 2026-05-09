





import java.util.List;
import java.util.ArrayList;

public class model_BookShelf  {

    private String name;





    private List<model_Book> model_books;




    private model_Book model_book;


    public model_BookShelf(
        String name    ) {
        this.name = name;
        this.model_books = new ArrayList<>();
    }

    public model_BookShelf(
        String name        ArrayList<model_Book> model_books    ) {
        this.name = name;
        this.model_books = model_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model_Book> getModel_books() {
        return model_books;
    }

    public void addModel_book(Model_book model_book) {
        this.model_books.add(model_book);
    }
    public model_Book getModel_book() {
        return model_book;
    }

    public void setModel_book(model_Book model_book) {
        this.model_book = model_book;
    }

}