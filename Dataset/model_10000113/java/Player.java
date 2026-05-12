





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None profile;
    private int money;
    private None hand;





    private Profile profile;




    private List<Hand> hands;


    public Player(
        None profile,        int money,        None hand    ) {
        this.profile = profile;
        this.money = money;
        this.hand = hand;
        this.hands = new ArrayList<>();
    }

    public Player(
        None profile,        int money,        None hand        ArrayList<Hand> hands    ) {
        this.profile = profile;
        this.money = money;
        this.hand = hand;
        this.hands = hands;
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

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }
    public List<Hand> getHands() {
        return hands;
    }

    public void addHand(Hand hand) {
        this.hands.add(hand);
    }

}