





import java.util.List;
import java.util.ArrayList;

public class Trick  {

    private String Card_5_;
    private None trickWinner;





    private Round round;


    public Trick(
        String Card_5_,        None trickWinner    ) {
        this.Card_5_ = Card_5_;
        this.trickWinner = trickWinner;
    }


    public String getCard_5_() {
        return Card_5_;
    }

    public void setCard_5_(String Card_5_) {
        this.Card_5_ = Card_5_;
    }
    public None getTrickwinner() {
        return trickWinner;
    }

    public void setTrickwinner(None trickWinner) {
        this.trickWinner = trickWinner;
    }

    public Round getRound() {
        return round;
    }

    public void setRound(Round round) {
        this.round = round;
    }

}