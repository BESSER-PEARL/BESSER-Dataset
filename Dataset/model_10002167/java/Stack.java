





import java.util.List;
import java.util.ArrayList;

public class Stack  {

    private int numOfCards;
    private None cards__;





    private Card card;




    private Stack stack;




    private Deck deck;


    public Stack(
        int numOfCards,        None cards__    ) {
        this.numOfCards = numOfCards;
        this.cards__ = cards__;
    }


    public int getNumofcards() {
        return numOfCards;
    }

    public void setNumofcards(int numOfCards) {
        this.numOfCards = numOfCards;
    }
    public None getCards__() {
        return cards__;
    }

    public void setCards__(None cards__) {
        this.cards__ = cards__;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }
    public Stack getStack() {
        return stack;
    }

    public void setStack(Stack stack) {
        this.stack = stack;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}