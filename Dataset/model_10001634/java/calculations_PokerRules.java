





import java.util.List;
import java.util.ArrayList;

public class calculations_PokerRules  {

    private None tableCardRank;
    private int numberOfPlayers;
    private String arrayWithHands;
    private String highestCardStraight;
    private String cardsOnTable;



    public calculations_PokerRules(
        None tableCardRank,        int numberOfPlayers,        String arrayWithHands,        String highestCardStraight,        String cardsOnTable    ) {
        this.tableCardRank = tableCardRank;
        this.numberOfPlayers = numberOfPlayers;
        this.arrayWithHands = arrayWithHands;
        this.highestCardStraight = highestCardStraight;
        this.cardsOnTable = cardsOnTable;
    }


    public None getTablecardrank() {
        return tableCardRank;
    }

    public void setTablecardrank(None tableCardRank) {
        this.tableCardRank = tableCardRank;
    }
    public int getNumberofplayers() {
        return numberOfPlayers;
    }

    public void setNumberofplayers(int numberOfPlayers) {
        this.numberOfPlayers = numberOfPlayers;
    }
    public String getArraywithhands() {
        return arrayWithHands;
    }

    public void setArraywithhands(String arrayWithHands) {
        this.arrayWithHands = arrayWithHands;
    }
    public String getHighestcardstraight() {
        return highestCardStraight;
    }

    public void setHighestcardstraight(String highestCardStraight) {
        this.highestCardStraight = highestCardStraight;
    }
    public String getCardsontable() {
        return cardsOnTable;
    }

    public void setCardsontable(String cardsOnTable) {
        this.cardsOnTable = cardsOnTable;
    }


}