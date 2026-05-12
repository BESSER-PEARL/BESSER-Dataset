





import java.util.List;
import java.util.ArrayList;

public class LoginPage  {

    private String User_name;





    private WELCOME_PAGE welcome_page;


    public LoginPage(
        String User_name    ) {
        this.User_name = User_name;
    }


    public String getUser_name() {
        return User_name;
    }

    public void setUser_name(String User_name) {
        this.User_name = User_name;
    }

    public WELCOME_PAGE getWelcome_page() {
        return welcome_page;
    }

    public void setWelcome_page(WELCOME_PAGE welcome_page) {
        this.welcome_page = welcome_page;
    }

}