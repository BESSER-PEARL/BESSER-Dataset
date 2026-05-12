





import java.util.List;
import java.util.ArrayList;

public class Guest  {

    private String Address;
    private String Name;



    public Guest(
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