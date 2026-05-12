





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String profile;
    private None hand;
    private int money;



    public Player(
        String profile,        None hand,        int money    ) {
        this.profile = profile;
        this.hand = hand;
        this.money = money;
    }


    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }


}