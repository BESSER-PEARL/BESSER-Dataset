





import java.util.List;
import java.util.ArrayList;

public class Play  {

    private int removedCard;
    private int Score;





    private Card_Interface card_interface;




    private playerTwo_external playertwo_external;




    private Deck deck;




    private playerOne_external playerone_external;




    private Players players;


    public Play(
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

    public Card_Interface getCard_interface() {
        return card_interface;
    }

    public void setCard_interface(Card_Interface card_interface) {
        this.card_interface = card_interface;
    }
    public playerTwo_external getPlayertwo_external() {
        return playertwo_external;
    }

    public void setPlayertwo_external(playerTwo_external playertwo_external) {
        this.playertwo_external = playertwo_external;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public playerOne_external getPlayerone_external() {
        return playerone_external;
    }

    public void setPlayerone_external(playerOne_external playerone_external) {
        this.playerone_external = playerone_external;
    }
    public Players getPlayers() {
        return players;
    }

    public void setPlayers(Players players) {
        this.players = players;
    }

}