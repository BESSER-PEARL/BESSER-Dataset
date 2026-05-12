





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private int phone;
    private String address;
    private String name;



    public Hospital(
        int phone,        String address,        String name    ) {
        this.phone = phone;
        this.address = address;
        this.name = name;
    }


    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}