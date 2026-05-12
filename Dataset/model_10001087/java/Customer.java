





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int phoneno;
    private String address;
    private int id;
    private String name;
    private String mailid;



    public Customer(
        int phoneno,        String address,        int id,        String name,        String mailid    ) {
        this.phoneno = phoneno;
        this.address = address;
        this.id = id;
        this.name = name;
        this.mailid = mailid;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMailid() {
        return mailid;
    }

    public void setMailid(String mailid) {
        this.mailid = mailid;
    }


}