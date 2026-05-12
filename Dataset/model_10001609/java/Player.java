





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None hand;
    private String profile;
    private int money;



    public Player(
        None hand,        String profile,        int money    ) {
        this.hand = hand;
        this.profile = profile;
        this.money = money;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }
    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }


}