





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Id;
    private String Address;
    private String Mobile_no___Email;
    private String Name;



    public Customer(
        String Id,        String Address,        String Mobile_no___Email,        String Name    ) {
        this.Id = Id;
        this.Address = Address;
        this.Mobile_no___Email = Mobile_no___Email;
        this.Name = Name;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getMobile_no___email() {
        return Mobile_no___Email;
    }

    public void setMobile_no___email(String Mobile_no___Email) {
        this.Mobile_no___Email = Mobile_no___Email;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}