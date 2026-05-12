





import java.util.List;
import java.util.ArrayList;

public class CardPlayer  {






    private List<Hand> hands;


    public CardPlayer(
    ) {
        this.hands = new ArrayList<>();
    }

    public CardPlayer(
        ArrayList<Hand> hands    ) {
        this.hands = hands;
    }


    public List<Hand> getHands() {
        return hands;
    }

    public void addHand(Hand hand) {
        this.hands.add(hand);
    }

}