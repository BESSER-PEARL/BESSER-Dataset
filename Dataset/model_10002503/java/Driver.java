





import java.util.List;
import java.util.ArrayList;

public class Driver  {

    private int Score;
    private int removedCard;





    private Players players;




    private Deck deck;




    private Card_Interface card_interface;


    public Driver(
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

    public Players getPlayers() {
        return players;
    }

    public void setPlayers(Players players) {
        this.players = players;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Card_Interface getCard_interface() {
        return card_interface;
    }

    public void setCard_interface(Card_Interface card_interface) {
        this.card_interface = card_interface;
    }

}