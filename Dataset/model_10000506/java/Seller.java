





import java.util.List;
import java.util.ArrayList;

public class Seller  {

    private int phoneno;
    private String address;
    private String mailid;
    private String name;
    private int id;
    private String T;





    private Customercare customercare;


    public Seller(
        int phoneno,        String address,        String mailid,        String name,        int id,        String T    ) {
        this.phoneno = phoneno;
        this.address = address;
        this.mailid = mailid;
        this.name = name;
        this.id = id;
        this.T = T;
    }


    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMailid() {
        return mailid;
    }

    public void setMailid(String mailid) {
        this.mailid = mailid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getT() {
        return T;
    }

    public void setT(String T) {
        this.T = T;
    }

    public Customercare getCustomercare() {
        return customercare;
    }

    public void setCustomercare(Customercare customercare) {
        this.customercare = customercare;
    }

}