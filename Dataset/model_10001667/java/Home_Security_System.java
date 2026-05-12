





import java.util.List;
import java.util.ArrayList;

public class Home_Security_System  {

    private int UserID;





    private Hub_Device hub_device;


    public Home_Security_System(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public Hub_Device getHub_device() {
        return hub_device;
    }

    public void setHub_device(Hub_Device hub_device) {
        this.hub_device = hub_device;
    }

}