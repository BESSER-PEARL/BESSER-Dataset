





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int id;
    private int phoneno;
    private String name;
    private String address;
    private String mailid;



    public Customer(
        int id,        int phoneno,        String name,        String address,        String mailid    ) {
        this.id = id;
        this.phoneno = phoneno;
        this.name = name;
        this.address = address;
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
    public String getMailid() {
        return mailid;
    }

    public void setMailid(String mailid) {
        this.mailid = mailid;
    }


}