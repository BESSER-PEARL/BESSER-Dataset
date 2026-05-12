





import java.util.List;
import java.util.ArrayList;

public class PARENT  {

    private int phoneNumber;
    private String id;
    private String password;



    public PARENT(
        int phoneNumber,        String id,        String password    ) {
        this.phoneNumber = phoneNumber;
        this.id = id;
        this.password = password;
    }


    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}