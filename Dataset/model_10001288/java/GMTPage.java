





import java.util.List;
import java.util.ArrayList;

public class GMTPage  {

    private String scSession_As_Greenway_Session_SessionClient;
    private float balance;



    public GMTPage(
        String scSession_As_Greenway_Session_SessionClient,        float balance    ) {
        this.scSession_As_Greenway_Session_SessionClient = scSession_As_Greenway_Session_SessionClient;
        this.balance = balance;
    }


    public String getScsession_as_greenway_session_sessionclient() {
        return scSession_As_Greenway_Session_SessionClient;
    }

    public void setScsession_as_greenway_session_sessionclient(String scSession_As_Greenway_Session_SessionClient) {
        this.scSession_As_Greenway_Session_SessionClient = scSession_As_Greenway_Session_SessionClient;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }


}