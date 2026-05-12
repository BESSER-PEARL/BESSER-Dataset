





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private None type;
    private String address;



    public Customer(
        String name,        None type,        String address    ) {
        this.name = name;
        this.type = type;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}