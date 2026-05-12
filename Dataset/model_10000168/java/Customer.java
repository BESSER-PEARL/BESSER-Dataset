





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private int ph_no;
    private String address;



    public Customer(
        String name,        int ph_no,        String address    ) {
        this.name = name;
        this.ph_no = ph_no;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPh_no() {
        return ph_no;
    }

    public void setPh_no(int ph_no) {
        this.ph_no = ph_no;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}