





import java.util.List;
import java.util.ArrayList;

public class Function  {

    private int Score;
    private int removedCard;





    private Card_Interface card_interface;




    private Deck deck;




    private Players players;


    public Function(
        int Score,        int removedCard    ) {
        this.Score = Score;
        this.removedCard = removedCard;
    }


    public int getScore() {
        return Score;
    }

    public void setScore(int Score) {
        this.Score = Score;
    }
    public int getRemovedcard() {
        return removedCard;
    }

    public void setRemovedcard(int removedCard) {
        this.removedCard = removedCard;
    }

    public Card_Interface getCard_interface() {
        return card_interface;
    }

    public void setCard_interface(Card_Interface card_interface) {
        this.card_interface = card_interface;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Players getPlayers() {
        return players;
    }

    public void setPlayers(Players players) {
        this.players = players;
    }

}