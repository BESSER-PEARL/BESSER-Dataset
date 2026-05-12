





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String shuffle;
    private String cards;
    private String random;
    private String random_cards;
    private String deck;
    private String deal_card;
    private String top_card;



    public Deck(
        String shuffle,        String cards,        String random,        String random_cards,        String deck,        String deal_card,        String top_card    ) {
        this.shuffle = shuffle;
        this.cards = cards;
        this.random = random;
        this.random_cards = random_cards;
        this.deck = deck;
        this.deal_card = deal_card;
        this.top_card = top_card;
    }


    public String getShuffle() {
        return shuffle;
    }

    public void setShuffle(String shuffle) {
        this.shuffle = shuffle;
    }
    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }
    public String getRandom() {
        return random;
    }

    public void setRandom(String random) {
        this.random = random;
    }
    public String getRandom_cards() {
        return random_cards;
    }

    public void setRandom_cards(String random_cards) {
        this.random_cards = random_cards;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getDeal_card() {
        return deal_card;
    }

    public void setDeal_card(String deal_card) {
        this.deal_card = deal_card;
    }
    public String getTop_card() {
        return top_card;
    }

    public void setTop_card(String top_card) {
        this.top_card = top_card;
    }


}