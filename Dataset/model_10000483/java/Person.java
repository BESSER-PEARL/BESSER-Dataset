





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String address;
    private String phone;



    public Person(
        String address,        String phone    ) {
        this.address = address;
        this.phone = phone;
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


}