





import java.util.List;
import java.util.ArrayList;

public class Home_Security_System  {

    private int UserID;





    private IOT iot;


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

    public IOT getIot() {
        return iot;
    }

    public void setIot(IOT iot) {
        this.iot = iot;
    }

}