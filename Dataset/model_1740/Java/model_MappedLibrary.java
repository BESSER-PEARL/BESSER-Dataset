





import java.util.List;
import java.util.ArrayList;

public class model_MappedLibrary  {

    private String books;





    private model_Location model_location;


    public model_MappedLibrary(
        String books    ) {
        this.books = books;
    }


    public String getBooks() {
        return books;
    }

    public void setBooks(String books) {
        this.books = books;
    }

    public model_Location getModel_location() {
        return model_location;
    }

    public void setModel_location(model_Location model_location) {
        this.model_location = model_location;
    }

}