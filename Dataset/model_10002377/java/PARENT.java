





import java.util.List;
import java.util.ArrayList;

public class PARENT  {

    private String id;
    private int phoneNumber;
    private String password;



    public PARENT(
        String id,        int phoneNumber,        String password    ) {
        this.id = id;
        this.phoneNumber = phoneNumber;
        this.password = password;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}