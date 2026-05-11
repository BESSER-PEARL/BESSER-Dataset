





import java.util.List;
import java.util.ArrayList;

public class model_User extends IEntity {

    private String password;
    private String userName;



    public model_User(
        String password,        String userName    ) {
        super(
        );
        this.password = password;
        this.userName = userName;
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


}