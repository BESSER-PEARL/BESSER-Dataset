





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String password;
    private String userName;
    private int id;



    public Customer(
        String password,        String userName,        int id    ) {
        this.password = password;
        this.userName = userName;
        this.id = id;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}