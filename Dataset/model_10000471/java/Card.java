





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String name;
    private String img;
    private String suit;
    private String val;



    public Card(
        String name,        String img,        String suit,        String val    ) {
        this.name = name;
        this.img = img;
        this.suit = suit;
        this.val = val;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getImg() {
        return img;
    }

    public void setImg(String img) {
        this.img = img;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }


}