





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String location;
    private String name;



    public Customer(
        String location,        String name    ) {
        this.location = location;
        this.name = name;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}