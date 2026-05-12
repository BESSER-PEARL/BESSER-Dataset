





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private String name;
    private None type;



    public Customer(
        String address,        String name,        None type    ) {
        this.address = address;
        this.name = name;
        this.type = type;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
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


}