





import java.util.List;
import java.util.ArrayList;

public class System_Controller_System_Controller  {

    private boolean GiveResponse;
    private boolean Database_Connection;



    public System_Controller_System_Controller(
        boolean GiveResponse,        boolean Database_Connection    ) {
        this.GiveResponse = GiveResponse;
        this.Database_Connection = Database_Connection;
    }


    public boolean getGiveresponse() {
        return GiveResponse;
    }

    public void setGiveresponse(boolean GiveResponse) {
        this.GiveResponse = GiveResponse;
    }
    public boolean getDatabase_connection() {
        return Database_Connection;
    }

    public void setDatabase_connection(boolean Database_Connection) {
        this.Database_Connection = Database_Connection;
    }


}