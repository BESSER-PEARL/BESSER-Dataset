





import java.util.List;
import java.util.ArrayList;

public class Function  {

    private int removedCard;
    private int Score;





    private PlayerUser_external playeruser_external;




    private Players players;




    private Deck deck;




    private Card_Interface card_interface;


    public Function(
        int removedCard,        int Score    ) {
        this.removedCard = removedCard;
        this.Score = Score;
    }


    public int getRemovedcard() {
        return removedCard;
    }

    public void setRemovedcard(int removedCard) {
        this.removedCard = removedCard;
    }
    public int getScore() {
        return Score;
    }

    public void setScore(int Score) {
        this.Score = Score;
    }

    public PlayerUser_external getPlayeruser_external() {
        return playeruser_external;
    }

    public void setPlayeruser_external(PlayerUser_external playeruser_external) {
        this.playeruser_external = playeruser_external;
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