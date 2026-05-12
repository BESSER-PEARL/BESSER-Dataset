





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private None cards;
    private int total;





    private List<Card> cards;




    private Dealer dealer;




    private Player player;


    public Hand(
        None cards,        int total    ) {
        this.cards = cards;
        this.total = total;
        this.cards = new ArrayList<>();
    }

    public Hand(
        None cards,        int total        ArrayList<Card> cards    ) {
        this.cards = cards;
        this.total = total;
        this.cards = cards;
    }

    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }
    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}