





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private String playerCards;
    private String dealerCards;





    private Deck deck;


    public Game(
        String playerCards,        String dealerCards    ) {
        this.playerCards = playerCards;
        this.dealerCards = dealerCards;
    }


    public String getPlayercards() {
        return playerCards;
    }

    public void setPlayercards(String playerCards) {
        this.playerCards = playerCards;
    }
    public String getDealercards() {
        return dealerCards;
    }

    public void setDealercards(String dealerCards) {
        this.dealerCards = dealerCards;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}