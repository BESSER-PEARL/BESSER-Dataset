





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Name;
    private String Address;



    public User(
        String Name,        String Address    ) {
        this.Name = Name;
        this.Address = Address;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}