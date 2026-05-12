





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int phoneno;
    private String mailid;
    private String name;
    private int id;
    private String address;



    public Customer(
        int phoneno,        String mailid,        String name,        int id,        String address    ) {
        this.phoneno = phoneno;
        this.mailid = mailid;
        this.name = name;
        this.id = id;
        this.address = address;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}