





import java.util.List;
import java.util.ArrayList;

public class model_DataBase  {






    private List<model_Book> model_books;


    public model_DataBase(
    ) {
        this.model_books = new ArrayList<>();
    }

    public model_DataBase(
        ArrayList<model_Book> model_books    ) {
        this.model_books = model_books;
    }


    public List<model_Book> getModel_books() {
        return model_books;
    }

    public void addModel_book(Model_book model_book) {
        this.model_books.add(model_book);
    }

}