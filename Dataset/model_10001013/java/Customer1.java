





import java.util.List;
import java.util.ArrayList;

public class Customer1  {

    private int customerId;
    private String name;
    private String address;
    private int phone;



    public Customer1(
        int customerId,        String name,        String address,        int phone    ) {
        this.customerId = customerId;
        this.name = name;
        this.address = address;
        this.phone = phone;
    }


    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }


}