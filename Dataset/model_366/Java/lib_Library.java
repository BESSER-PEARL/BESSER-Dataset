





import java.util.List;
import java.util.ArrayList;

public class lib_Library  {

    private String name;
    private String location;



    public lib_Library(
        String name,        String location    ) {
        this.name = name;
        this.location = location;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}