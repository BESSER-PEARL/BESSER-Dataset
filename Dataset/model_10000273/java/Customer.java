





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private int ph_no;
    private String name;



    public Customer(
        String address,        int ph_no,        String name    ) {
        this.address = address;
        this.ph_no = ph_no;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPh_no() {
        return ph_no;
    }

    public void setPh_no(int ph_no) {
        this.ph_no = ph_no;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}