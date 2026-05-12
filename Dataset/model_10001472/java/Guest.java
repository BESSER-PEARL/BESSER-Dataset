





import java.util.List;
import java.util.ArrayList;

public class Guest  {

    private String Name;
    private String Address;



    public Guest(
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