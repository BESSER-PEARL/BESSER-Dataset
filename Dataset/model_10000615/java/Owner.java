





import java.util.List;
import java.util.ArrayList;

public class Owner  {

    private String name;
    private String Address;





    private Property property;


    public Owner(
        String name,        String Address    ) {
        this.name = name;
        this.Address = Address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}