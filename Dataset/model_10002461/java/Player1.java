





import java.util.List;
import java.util.ArrayList;

public class Player1  {

    private String hand;
    private String name;





    private List<Card1> card1s;




    private List<Game1> game1s;




    private Avatar1 avatar1;


    public Player1(
        String hand,        String name    ) {
        this.hand = hand;
        this.name = name;
        this.card1s = new ArrayList<>();
        this.game1s = new ArrayList<>();
    }

    public Player1(
        String hand,        String name        ArrayList<Card1> card1s,        ArrayList<Game1> game1s    ) {
        this.hand = hand;
        this.name = name;
        this.card1s = card1s;
        this.game1s = game1s;
    }

    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Card1> getCard1s() {
        return card1s;
    }

    public void addCard1(Card1 card1) {
        this.card1s.add(card1);
    }
    public List<Game1> getGame1s() {
        return game1s;
    }

    public void addGame1(Game1 game1) {
        this.game1s.add(game1);
    }
    public Avatar1 getAvatar1() {
        return avatar1;
    }

    public void setAvatar1(Avatar1 avatar1) {
        this.avatar1 = avatar1;
    }

}