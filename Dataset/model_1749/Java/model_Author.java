





import java.util.List;
import java.util.ArrayList;

public class model_Author  {

    private String lastName;
    private String firstName;





    private model_Book model_book;


    public model_Author(
        String lastName,        String firstName    ) {
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public model_Book getModel_book() {
        return model_book;
    }

    public void setModel_book(model_Book model_book) {
        this.model_book = model_book;
    }

}