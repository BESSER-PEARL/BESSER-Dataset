





import java.util.List;
import java.util.ArrayList;

public class PitchDealer  {

    private None SelectDealer;
    private None displaycard;
    private None Randomcards;



    public PitchDealer(
        None SelectDealer,        None displaycard,        None Randomcards    ) {
        this.SelectDealer = SelectDealer;
        this.displaycard = displaycard;
        this.Randomcards = Randomcards;
    }


    public None getSelectdealer() {
        return SelectDealer;
    }

    public void setSelectdealer(None SelectDealer) {
        this.SelectDealer = SelectDealer;
    }
    public None getDisplaycard() {
        return displaycard;
    }

    public void setDisplaycard(None displaycard) {
        this.displaycard = displaycard;
    }
    public None getRandomcards() {
        return Randomcards;
    }

    public void setRandomcards(None Randomcards) {
        this.Randomcards = Randomcards;
    }


}