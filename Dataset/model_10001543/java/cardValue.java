





import java.util.List;
import java.util.ArrayList;

public class cardValue  {

    private None Jack;
    private None King;
    private None Ace;
    private None Queen;



    public cardValue(
        None Jack,        None King,        None Ace,        None Queen    ) {
        this.Jack = Jack;
        this.King = King;
        this.Ace = Ace;
        this.Queen = Queen;
    }


    public None getJack() {
        return Jack;
    }

    public void setJack(None Jack) {
        this.Jack = Jack;
    }
    public None getKing() {
        return King;
    }

    public void setKing(None King) {
        this.King = King;
    }
    public None getAce() {
        return Ace;
    }

    public void setAce(None Ace) {
        this.Ace = Ace;
    }
    public None getQueen() {
        return Queen;
    }

    public void setQueen(None Queen) {
        this.Queen = Queen;
    }


}