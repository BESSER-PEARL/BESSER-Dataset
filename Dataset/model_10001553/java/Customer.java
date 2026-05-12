





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int phoneno;
    private int id;
    private String name;
    private String mailid;
    private String address;



    public Customer(
        int phoneno,        int id,        String name,        String mailid,        String address    ) {
        this.phoneno = phoneno;
        this.id = id;
        this.name = name;
        this.mailid = mailid;
        this.address = address;
    }


    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}