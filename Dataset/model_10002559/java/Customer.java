





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private String address;
    private None type;



    public Customer(
        String name,        String address,        None type    ) {
        this.name = name;
        this.address = address;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}