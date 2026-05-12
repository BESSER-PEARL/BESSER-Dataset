





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int money;
    private None hand;
    private None profile;



    public Player(
        int money,        None hand,        None profile    ) {
        this.money = money;
        this.hand = hand;
        this.profile = profile;
    }


    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public None getProfile() {
        return profile;
    }

    public void setProfile(None profile) {
        this.profile = profile;
    }


}