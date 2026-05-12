





import java.util.List;
import java.util.ArrayList;

public class Customer1  {

    private String address;
    private int customerId;
    private String name;
    private int phone;



    public Customer1(
        String address,        int customerId,        String name,        int phone    ) {
        this.address = address;
        this.customerId = customerId;
        this.name = name;
        this.phone = phone;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }


}