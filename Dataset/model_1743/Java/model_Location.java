





import java.util.List;
import java.util.ArrayList;

public class model_Location  {

    private String id;
    private String address;





    private model_Book model_book;




    private model_Library model_library;


    public model_Location(
        String id,        String address    ) {
        this.id = id;
        this.address = address;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public model_Book getModel_book() {
        return model_book;
    }

    public void setModel_book(model_Book model_book) {
        this.model_book = model_book;
    }
    public model_Library getModel_library() {
        return model_library;
    }

    public void setModel_library(model_Library model_library) {
        this.model_library = model_library;
    }

}