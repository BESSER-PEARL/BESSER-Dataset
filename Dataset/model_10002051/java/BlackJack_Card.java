





import java.util.List;
import java.util.ArrayList;

public class BlackJack_Card  {

    private int value;
    private String color;
    private int rank;





    private List<BlackJack_Hand> blackjack_hands;


    public BlackJack_Card(
        int value,        String color,        int rank    ) {
        this.value = value;
        this.color = color;
        this.rank = rank;
        this.blackjack_hands = new ArrayList<>();
    }

    public BlackJack_Card(
        int value,        String color,        int rank        ArrayList<BlackJack_Hand> blackjack_hands    ) {
        this.value = value;
        this.color = color;
        this.rank = rank;
        this.blackjack_hands = blackjack_hands;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public List<BlackJack_Hand> getBlackjack_hands() {
        return blackjack_hands;
    }

    public void addBlackjack_hand(Blackjack_hand blackjack_hand) {
        this.blackjack_hands.add(blackjack_hand);
    }

}