





import java.util.List;
import java.util.ArrayList;

public class Memory_Interface  {






    private List<Web_User> web_users;


    public Memory_Interface(
    ) {
        this.web_users = new ArrayList<>();
    }

    public Memory_Interface(
        ArrayList<Web_User> web_users    ) {
        this.web_users = web_users;
    }


    public List<Web_User> getWeb_users() {
        return web_users;
    }

    public void addWeb_user(Web_user web_user) {
        this.web_users.add(web_user);
    }

}