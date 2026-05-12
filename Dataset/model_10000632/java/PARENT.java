





import java.util.List;
import java.util.ArrayList;

public class PARENT  {

    private int phoneNumber;
    private String password;
    private String id;



    public PARENT(
        int phoneNumber,        String password,        String id    ) {
        this.phoneNumber = phoneNumber;
        this.password = password;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}