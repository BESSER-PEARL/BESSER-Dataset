





import java.util.List;
import java.util.ArrayList;

public class patron  {

    private String Name;
    private int Contact_number;
    private String Address;



    public patron(
        String Name,        int Contact_number,        String Address    ) {
        this.Name = Name;
        this.Contact_number = Contact_number;
        this.Address = Address;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getContact_number() {
        return Contact_number;
    }

    public void setContact_number(int Contact_number) {
        this.Contact_number = Contact_number;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}