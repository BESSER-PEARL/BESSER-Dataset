





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int score;
    private String hand;





    private Game game;




    private List<Card> cards;


    public Player(
        int score,        String hand    ) {
        this.score = score;
        this.hand = hand;
        this.cards = new ArrayList<>();
    }

    public Player(
        int score,        String hand        ArrayList<Card> cards    ) {
        this.score = score;
        this.hand = hand;
        this.cards = cards;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }
    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}