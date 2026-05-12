





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String mailid;
    private int phoneno;
    private String name;
    private int id;
    private String address;



    public Client(
        String mailid,        int phoneno,        String name,        int id,        String address    ) {
        this.mailid = mailid;
        this.phoneno = phoneno;
        this.name = name;
        this.id = id;
        this.address = address;
    }


    public String getMailid() {
        return mailid;
    }

    public void setMailid(String mailid) {
        this.mailid = mailid;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}