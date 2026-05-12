





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String contents;





    private List<Card> cards;


    public Group(
        String contents    ) {
        this.contents = contents;
        this.cards = new ArrayList<>();
    }

    public Group(
        String contents        ArrayList<Card> cards    ) {
        this.contents = contents;
        this.cards = cards;
    }

    public String getContents() {
        return contents;
    }

    public void setContents(String contents) {
        this.contents = contents;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}