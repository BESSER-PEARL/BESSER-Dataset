





import java.util.List;
import java.util.ArrayList;

public class MemoryGame_Deck  {

    private int id;
    private None cards;
    private String image;





    private List<MemoryGame_Card> memorygame_cards;


    public MemoryGame_Deck(
        int id,        None cards,        String image    ) {
        this.id = id;
        this.cards = cards;
        this.image = image;
        this.memorygame_cards = new ArrayList<>();
    }

    public MemoryGame_Deck(
        int id,        None cards,        String image        ArrayList<MemoryGame_Card> memorygame_cards    ) {
        this.id = id;
        this.cards = cards;
        this.image = image;
        this.memorygame_cards = memorygame_cards;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public List<MemoryGame_Card> getMemorygame_cards() {
        return memorygame_cards;
    }

    public void addMemorygame_card(Memorygame_card memorygame_card) {
        this.memorygame_cards.add(memorygame_card);
    }

}