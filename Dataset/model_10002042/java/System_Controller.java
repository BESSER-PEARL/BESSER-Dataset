





import java.util.List;
import java.util.ArrayList;

public class System_Controller  {

    private boolean Database_Connection;
    private boolean GiveResponse;





    private User_Controller user_controller;


    public System_Controller(
        boolean Database_Connection,        boolean GiveResponse    ) {
        this.Database_Connection = Database_Connection;
        this.GiveResponse = GiveResponse;
    }


    public boolean getDatabase_connection() {
        return Database_Connection;
    }

    public void setDatabase_connection(boolean Database_Connection) {
        this.Database_Connection = Database_Connection;
    }
    public boolean getGiveresponse() {
        return GiveResponse;
    }

    public void setGiveresponse(boolean GiveResponse) {
        this.GiveResponse = GiveResponse;
    }

    public User_Controller getUser_controller() {
        return user_controller;
    }

    public void setUser_controller(User_Controller user_controller) {
        this.user_controller = user_controller;
    }

}