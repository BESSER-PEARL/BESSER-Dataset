





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int phoneno;
    private String mailid;
    private String name;
    private String address;
    private int id;



    public Customer(
        int phoneno,        String mailid,        String name,        String address,        int id    ) {
        this.phoneno = phoneno;
        this.mailid = mailid;
        this.name = name;
        this.address = address;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}