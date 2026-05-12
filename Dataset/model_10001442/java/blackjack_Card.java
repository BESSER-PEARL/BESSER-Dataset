





import java.util.List;
import java.util.ArrayList;

public class blackjack_Card  {

    private int MAX_VALUE_OF_ACE;
    private int BLACKJACK_VALUE;
    private None suit;
    private None value;



    public blackjack_Card(
        int MAX_VALUE_OF_ACE,        int BLACKJACK_VALUE,        None suit,        None value    ) {
        this.MAX_VALUE_OF_ACE = MAX_VALUE_OF_ACE;
        this.BLACKJACK_VALUE = BLACKJACK_VALUE;
        this.suit = suit;
        this.value = value;
    }


    public int getMax_value_of_ace() {
        return MAX_VALUE_OF_ACE;
    }

    public void setMax_value_of_ace(int MAX_VALUE_OF_ACE) {
        this.MAX_VALUE_OF_ACE = MAX_VALUE_OF_ACE;
    }
    public int getBlackjack_value() {
        return BLACKJACK_VALUE;
    }

    public void setBlackjack_value(int BLACKJACK_VALUE) {
        this.BLACKJACK_VALUE = BLACKJACK_VALUE;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public None getValue() {
        return value;
    }

    public void setValue(None value) {
        this.value = value;
    }


}