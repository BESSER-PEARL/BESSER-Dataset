





import java.util.List;
import java.util.ArrayList;

public class MemoryGame_Card  {

    private int position;
    private boolean isShowing;
    private String image;
    private None deck;
    private int id;



    public MemoryGame_Card(
        int position,        boolean isShowing,        String image,        None deck,        int id    ) {
        this.position = position;
        this.isShowing = isShowing;
        this.image = image;
        this.deck = deck;
        this.id = id;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public boolean getIsshowing() {
        return isShowing;
    }

    public void setIsshowing(boolean isShowing) {
        this.isShowing = isShowing;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}