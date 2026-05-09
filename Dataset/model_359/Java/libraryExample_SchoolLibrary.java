





import java.util.List;
import java.util.ArrayList;

public class libraryExample_SchoolLibrary extends Library {

    private String location;



    public libraryExample_SchoolLibrary(
        String location    ) {
        super(
        );
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}