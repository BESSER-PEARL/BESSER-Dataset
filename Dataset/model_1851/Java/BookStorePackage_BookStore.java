





import java.util.List;
import java.util.ArrayList;

public class BookStorePackage_BookStore  {

    private String owner;
    private String location;



    public BookStorePackage_BookStore(
        String owner,        String location    ) {
        this.owner = owner;
        this.location = location;
    }


    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}