





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String mailid;
    private String name;
    private String address;
    private int id;



    public Customer(
        String mailid,        String name,        String address,        int id    ) {
        this.mailid = mailid;
        this.name = name;
        this.address = address;
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