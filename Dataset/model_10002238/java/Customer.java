





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String mailid;
    private String address;
    private int phoneno;
    private String name;
    private int id;



    public Customer(
        String mailid,        String address,        int phoneno,        String name,        int id    ) {
        this.mailid = mailid;
        this.address = address;
        this.phoneno = phoneno;
        this.name = name;
        this.id = id;
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
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
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


}