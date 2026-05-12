





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private String dealerCards;
    private String playerCards;





    private Deck deck;


    public Game(
        String dealerCards,        String playerCards    ) {
        this.dealerCards = dealerCards;
        this.playerCards = playerCards;
    }


    public String getDealercards() {
        return dealerCards;
    }

    public void setDealercards(String dealerCards) {
        this.dealerCards = dealerCards;
    }
    public String getPlayercards() {
        return playerCards;
    }

    public void setPlayercards(String playerCards) {
        this.playerCards = playerCards;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}