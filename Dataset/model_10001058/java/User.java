





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;
    private String email;
    private int id;
    private int phnNo;
    private String address;



    public User(
        String name,        String email,        int id,        int phnNo,        String address    ) {
        this.name = name;
        this.email = email;
        this.id = id;
        this.phnNo = phnNo;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPhnno() {
        return phnNo;
    }

    public void setPhnno(int phnNo) {
        this.phnNo = phnNo;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}