





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private int id;
    private String mailid;
    private String name;
    private int phoneno;



    public Customer(
        String address,        int id,        String mailid,        String name,        int phoneno    ) {
        this.address = address;
        this.id = id;
        this.mailid = mailid;
        this.name = name;
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
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }


}