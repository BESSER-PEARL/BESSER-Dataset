





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String mailid;
    private int id;
    private int phoneno;
    private String address;
    private String name;



    public Customer(
        String mailid,        int id,        int phoneno,        String address,        String name    ) {
        this.mailid = mailid;
        this.id = id;
        this.phoneno = phoneno;
        this.address = address;
        this.name = name;
    }


    public String getMailid() {
        return mailid;
    }

    public void setMailid(String mailid) {
        this.mailid = mailid;
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