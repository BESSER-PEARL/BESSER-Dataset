





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private int phoneno;
    private String address;
    private String mailid;
    private int id;



    public Customer(
        String name,        int phoneno,        String address,        String mailid,        int id    ) {
        this.name = name;
        this.phoneno = phoneno;
        this.address = address;
        this.mailid = mailid;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}