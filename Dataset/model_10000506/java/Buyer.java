





import java.util.List;
import java.util.ArrayList;

public class Buyer  {

    private String name;
    private String T;
    private int id;
    private String address;
    private String mailid;
    private int phoneno;



    public Buyer(
        String name,        String T,        int id,        String address,        String mailid,        int phoneno    ) {
        this.name = name;
        this.T = T;
        this.id = id;
        this.address = address;
        this.mailid = mailid;
        this.phoneno = phoneno;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getT() {
        return T;
    }

    public void setT(String T) {
        this.T = T;
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


}