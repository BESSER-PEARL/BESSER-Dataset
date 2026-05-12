





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None mainDeck;
    private None cardsOnTable;
    private None completedCards;



    public Game(
        None mainDeck,        None cardsOnTable,        None completedCards    ) {
        this.mainDeck = mainDeck;
        this.cardsOnTable = cardsOnTable;
        this.completedCards = completedCards;
    }


    public None getMaindeck() {
        return mainDeck;
    }

    public void setMaindeck(None mainDeck) {
        this.mainDeck = mainDeck;
    }
    public None getCardsontable() {
        return cardsOnTable;
    }

    public void setCardsontable(None cardsOnTable) {
        this.cardsOnTable = cardsOnTable;
    }
    public None getCompletedcards() {
        return completedCards;
    }

    public void setCompletedcards(None completedCards) {
        this.completedCards = completedCards;
    }


}