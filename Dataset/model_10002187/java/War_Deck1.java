





import java.util.List;
import java.util.ArrayList;

public class War_Deck1  {

    private int LOWEST_NUMERIC_VALUE1;
    private int NUMERIC_CARDS_IN_SUIT;
    private int NUMERIC_CARDS_IN_SUIT1;
    private int TOP_CARD;
    private int TOP_CARD1;
    private int LOWEST_NUMERIC_VALUE;





    private List<War_Card1> war_card1s;




    private List<War_Card1> war_card1s;




    private War_Card1 war_card1;




    private War_Card1 war_card1;


    public War_Deck1(
        int LOWEST_NUMERIC_VALUE1,        int NUMERIC_CARDS_IN_SUIT,        int NUMERIC_CARDS_IN_SUIT1,        int TOP_CARD,        int TOP_CARD1,        int LOWEST_NUMERIC_VALUE    ) {
        this.LOWEST_NUMERIC_VALUE1 = LOWEST_NUMERIC_VALUE1;
        this.NUMERIC_CARDS_IN_SUIT = NUMERIC_CARDS_IN_SUIT;
        this.NUMERIC_CARDS_IN_SUIT1 = NUMERIC_CARDS_IN_SUIT1;
        this.TOP_CARD = TOP_CARD;
        this.TOP_CARD1 = TOP_CARD1;
        this.LOWEST_NUMERIC_VALUE = LOWEST_NUMERIC_VALUE;
        this.war_card1s = new ArrayList<>();
        this.war_card1s = new ArrayList<>();
    }

    public War_Deck1(
        int LOWEST_NUMERIC_VALUE1,        int NUMERIC_CARDS_IN_SUIT,        int NUMERIC_CARDS_IN_SUIT1,        int TOP_CARD,        int TOP_CARD1,        int LOWEST_NUMERIC_VALUE        ArrayList<War_Card1> war_card1s,        ArrayList<War_Card1> war_card1s    ) {
        this.LOWEST_NUMERIC_VALUE1 = LOWEST_NUMERIC_VALUE1;
        this.NUMERIC_CARDS_IN_SUIT = NUMERIC_CARDS_IN_SUIT;
        this.NUMERIC_CARDS_IN_SUIT1 = NUMERIC_CARDS_IN_SUIT1;
        this.TOP_CARD = TOP_CARD;
        this.TOP_CARD1 = TOP_CARD1;
        this.LOWEST_NUMERIC_VALUE = LOWEST_NUMERIC_VALUE;
        this.war_card1s = war_card1s;
        this.war_card1s = war_card1s;
    }

    public int getLowest_numeric_value1() {
        return LOWEST_NUMERIC_VALUE1;
    }

    public void setLowest_numeric_value1(int LOWEST_NUMERIC_VALUE1) {
        this.LOWEST_NUMERIC_VALUE1 = LOWEST_NUMERIC_VALUE1;
    }
    public int getNumeric_cards_in_suit() {
        return NUMERIC_CARDS_IN_SUIT;
    }

    public void setNumeric_cards_in_suit(int NUMERIC_CARDS_IN_SUIT) {
        this.NUMERIC_CARDS_IN_SUIT = NUMERIC_CARDS_IN_SUIT;
    }
    public int getNumeric_cards_in_suit1() {
        return NUMERIC_CARDS_IN_SUIT1;
    }

    public void setNumeric_cards_in_suit1(int NUMERIC_CARDS_IN_SUIT1) {
        this.NUMERIC_CARDS_IN_SUIT1 = NUMERIC_CARDS_IN_SUIT1;
    }
    public int getTop_card() {
        return TOP_CARD;
    }

    public void setTop_card(int TOP_CARD) {
        this.TOP_CARD = TOP_CARD;
    }
    public int getTop_card1() {
        return TOP_CARD1;
    }

    public void setTop_card1(int TOP_CARD1) {
        this.TOP_CARD1 = TOP_CARD1;
    }
    public int getLowest_numeric_value() {
        return LOWEST_NUMERIC_VALUE;
    }

    public void setLowest_numeric_value(int LOWEST_NUMERIC_VALUE) {
        this.LOWEST_NUMERIC_VALUE = LOWEST_NUMERIC_VALUE;
    }

    public List<War_Card1> getWar_card1s() {
        return war_card1s;
    }

    public void addWar_card1(War_card1 war_card1) {
        this.war_card1s.add(war_card1);
    }
    public List<War_Card1> getWar_card1s() {
        return war_card1s;
    }

    public void addWar_card1(War_card1 war_card1) {
        this.war_card1s.add(war_card1);
    }
    public War_Card1 getWar_card1() {
        return war_card1;
    }

    public void setWar_card1(War_Card1 war_card1) {
        this.war_card1 = war_card1;
    }
    public War_Card1 getWar_card1() {
        return war_card1;
    }

    public void setWar_card1(War_Card1 war_card1) {
        this.war_card1 = war_card1;
    }

}