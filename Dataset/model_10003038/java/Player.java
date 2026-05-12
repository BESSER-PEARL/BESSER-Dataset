





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None profile;
    private None hand;
    private int money;



    public Player(
        None profile,        None hand,        int money    ) {
        this.profile = profile;
        this.hand = hand;
        this.money = money;
    }


    public None getProfile() {
        return profile;
    }

    public void setProfile(None profile) {
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