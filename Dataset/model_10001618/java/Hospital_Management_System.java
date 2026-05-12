





import java.util.List;
import java.util.ArrayList;

public class Hospital_Management_System  {

    private String Address;
    private String Name;
    private String Code;



    public Hospital_Management_System(
        String Address,        String Name,        String Code    ) {
        this.Address = Address;
        this.Name = Name;
        this.Code = Code;
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
    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }


}