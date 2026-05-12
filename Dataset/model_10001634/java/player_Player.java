





import java.util.List;
import java.util.ArrayList;

public class player_Player  {

    private None state;
    private float wealth;
    private float bigB;
    private int observerIDTracker;
    private int observerID;
    private String name;
    private boolean dealer;





    private common_Hand common_hand;




    private managers_LoginManager managers_loginmanager;




    private managers_GameManager managers_gamemanager;


    public player_Player(
        None state,        float wealth,        float bigB,        int observerIDTracker,        int observerID,        String name,        boolean dealer    ) {
        this.state = state;
        this.wealth = wealth;
        this.bigB = bigB;
        this.observerIDTracker = observerIDTracker;
        this.observerID = observerID;
        this.name = name;
        this.dealer = dealer;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public float getWealth() {
        return wealth;
    }

    public void setWealth(float wealth) {
        this.wealth = wealth;
    }
    public float getBigb() {
        return bigB;
    }

    public void setBigb(float bigB) {
        this.bigB = bigB;
    }
    public int getObserveridtracker() {
        return observerIDTracker;
    }

    public void setObserveridtracker(int observerIDTracker) {
        this.observerIDTracker = observerIDTracker;
    }
    public int getObserverid() {
        return observerID;
    }

    public void setObserverid(int observerID) {
        this.observerID = observerID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDealer() {
        return dealer;
    }

    public void setDealer(boolean dealer) {
        this.dealer = dealer;
    }

    public common_Hand getCommon_hand() {
        return common_hand;
    }

    public void setCommon_hand(common_Hand common_hand) {
        this.common_hand = common_hand;
    }
    public managers_LoginManager getManagers_loginmanager() {
        return managers_loginmanager;
    }

    public void setManagers_loginmanager(managers_LoginManager managers_loginmanager) {
        this.managers_loginmanager = managers_loginmanager;
    }
    public managers_GameManager getManagers_gamemanager() {
        return managers_gamemanager;
    }

    public void setManagers_gamemanager(managers_GameManager managers_gamemanager) {
        this.managers_gamemanager = managers_gamemanager;
    }

}