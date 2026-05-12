





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int id;
    private int phoneno;
    private String mailid;
    private String address;
    private String name;



    public Customer(
        int id,        int phoneno,        String mailid,        String address,        String name    ) {
        this.id = id;
        this.phoneno = phoneno;
        this.mailid = mailid;
        this.address = address;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getMailid() {
        return mailid;
    }

    public void setMailid(String mailid) {
        this.mailid = mailid;
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