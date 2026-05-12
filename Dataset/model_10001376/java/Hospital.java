





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String Address;
    private String name;
    private String phone_no;



    public Hospital(
        String Address,        String name,        String phone_no    ) {
        this.Address = Address;
        this.name = name;
        this.phone_no = phone_no;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(String phone_no) {
        this.phone_no = phone_no;
    }


}