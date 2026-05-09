





import java.util.List;
import java.util.ArrayList;

public class bookstore_Ent  {

    private String name;





    private bookstore_Model bookstore_model;


    public bookstore_Ent(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bookstore_Model getBookstore_model() {
        return bookstore_model;
    }

    public void setBookstore_model(bookstore_Model bookstore_model) {
        this.bookstore_model = bookstore_model;
    }

}