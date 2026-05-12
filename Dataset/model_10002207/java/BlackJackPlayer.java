





import java.util.List;
import java.util.ArrayList;

public class BlackJackPlayer  {

    private int MaxNumCards;
    private None cards__;
    private int cardCount;





    private BlackJack blackjack;


    public BlackJackPlayer(
        int MaxNumCards,        None cards__,        int cardCount    ) {
        this.MaxNumCards = MaxNumCards;
        this.cards__ = cards__;
        this.cardCount = cardCount;
    }


    public int getMaxnumcards() {
        return MaxNumCards;
    }

    public void setMaxnumcards(int MaxNumCards) {
        this.MaxNumCards = MaxNumCards;
    }
    public None getCards__() {
        return cards__;
    }

    public void setCards__(None cards__) {
        this.cards__ = cards__;
    }
    public int getCardcount() {
        return cardCount;
    }

    public void setCardcount(int cardCount) {
        this.cardCount = cardCount;
    }

    public BlackJack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(BlackJack blackjack) {
        this.blackjack = blackjack;
    }

}