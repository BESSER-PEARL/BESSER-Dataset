





import java.util.List;
import java.util.ArrayList;

public class player_Players  {

    private int MaxAmountOfPlayers;
    private int AmountOfPlayers;
    private boolean goodToGo;
    private float wealth;





    private managers_LoginManager managers_loginmanager;




    private managers_GameManager managers_gamemanager;




    private List<common_Observer_Interface> common_observer_interfaces;




    private managers_GameManager managers_gamemanager;


    public player_Players(
        int MaxAmountOfPlayers,        int AmountOfPlayers,        boolean goodToGo,        float wealth    ) {
        this.MaxAmountOfPlayers = MaxAmountOfPlayers;
        this.AmountOfPlayers = AmountOfPlayers;
        this.goodToGo = goodToGo;
        this.wealth = wealth;
        this.common_observer_interfaces = new ArrayList<>();
    }

    public player_Players(
        int MaxAmountOfPlayers,        int AmountOfPlayers,        boolean goodToGo,        float wealth        ArrayList<common_Observer_Interface> common_observer_interfaces    ) {
        this.MaxAmountOfPlayers = MaxAmountOfPlayers;
        this.AmountOfPlayers = AmountOfPlayers;
        this.goodToGo = goodToGo;
        this.wealth = wealth;
        this.common_observer_interfaces = common_observer_interfaces;
    }

    public int getMaxamountofplayers() {
        return MaxAmountOfPlayers;
    }

    public void setMaxamountofplayers(int MaxAmountOfPlayers) {
        this.MaxAmountOfPlayers = MaxAmountOfPlayers;
    }
    public int getAmountofplayers() {
        return AmountOfPlayers;
    }

    public void setAmountofplayers(int AmountOfPlayers) {
        this.AmountOfPlayers = AmountOfPlayers;
    }
    public boolean getGoodtogo() {
        return goodToGo;
    }

    public void setGoodtogo(boolean goodToGo) {
        this.goodToGo = goodToGo;
    }
    public float getWealth() {
        return wealth;
    }

    public void setWealth(float wealth) {
        this.wealth = wealth;
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
    public List<common_Observer_Interface> getCommon_observer_interfaces() {
        return common_observer_interfaces;
    }

    public void addCommon_observer_interface(Common_observer_interface common_observer_interface) {
        this.common_observer_interfaces.add(common_observer_interface);
    }
    public managers_GameManager getManagers_gamemanager() {
        return managers_gamemanager;
    }

    public void setManagers_gamemanager(managers_GameManager managers_gamemanager) {
        this.managers_gamemanager = managers_gamemanager;
    }

}