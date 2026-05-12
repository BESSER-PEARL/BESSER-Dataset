





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String login;
    private int password;
    private int creationDate;





    private User user;


    public Account(
        String login,        int password,        int creationDate    ) {
        this.login = login;
        this.password = password;
        this.creationDate = creationDate;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public int getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(int creationDate) {
        this.creationDate = creationDate;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}