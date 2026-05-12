





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String players;
    private int id;
    private String attribute;
    private String attribute2;
    private String cards;





    private List<Hand> hands;




    private Game game;


    public Deck(
        String players,        int id,        String attribute,        String attribute2,        String cards    ) {
        this.players = players;
        this.id = id;
        this.attribute = attribute;
        this.attribute2 = attribute2;
        this.cards = cards;
        this.hands = new ArrayList<>();
    }

    public Deck(
        String players,        int id,        String attribute,        String attribute2,        String cards        ArrayList<Hand> hands    ) {
        this.players = players;
        this.id = id;
        this.attribute = attribute;
        this.attribute2 = attribute2;
        this.cards = cards;
        this.hands = hands;
    }

    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }

    public List<Hand> getHands() {
        return hands;
    }

    public void addHand(Hand hand) {
        this.hands.add(hand);
    }
    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

}