





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Address;
    private String Name;



    public User(
        String Address,        String Name    ) {
        this.Address = Address;
        this.Name = Name;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}