





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String mailid;
    private int id;
    private String name;
    private String address;
    private int phoneno;



    public Customer(
        String mailid,        int id,        String name,        String address,        int phoneno    ) {
        this.mailid = mailid;
        this.id = id;
        this.name = name;
        this.address = address;
        this.phoneno = phoneno;
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
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }


}