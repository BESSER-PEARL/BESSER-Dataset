





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None profile;
    private int money;
    private None hand;



    public Player(
        None profile,        int money,        None hand    ) {
        this.profile = profile;
        this.money = money;
        this.hand = hand;
    }


    public None getProfile() {
        return profile;
    }

    public void setProfile(None profile) {
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


}