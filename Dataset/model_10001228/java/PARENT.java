





import java.util.List;
import java.util.ArrayList;

public class PARENT  {

    private String password;
    private int phoneNumber;
    private String id;



    public PARENT(
        String password,        int phoneNumber,        String id    ) {
        this.password = password;
        this.phoneNumber = phoneNumber;
        this.id = id;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
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


}