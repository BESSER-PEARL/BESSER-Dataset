





import java.util.List;
import java.util.ArrayList;

public class Factory_Security_System  {

    private int UserID;





    private Gateway gateway;


    public Factory_Security_System(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public Gateway getGateway() {
        return gateway;
    }

    public void setGateway(Gateway gateway) {
        this.gateway = gateway;
    }

}