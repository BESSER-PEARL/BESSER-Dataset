





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String address;
    private String phone;
    private String name;



    public Hospital(
        String address,        String phone,        String name    ) {
        this.address = address;
        this.phone = phone;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}