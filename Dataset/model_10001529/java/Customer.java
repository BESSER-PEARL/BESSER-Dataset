





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String userName;
    private String password;
    private int id;



    public Customer(
        String userName,        String password,        int id    ) {
        this.userName = userName;
        this.password = password;
        this.id = id;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}