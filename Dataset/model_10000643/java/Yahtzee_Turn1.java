





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Turn1  {

    private String Dice;





    private Yahtzee_Display1 yahtzee_display1;


    public Yahtzee_Turn1(
        String Dice    ) {
        this.Dice = Dice;
    }


    public String getDice() {
        return Dice;
    }

    public void setDice(String Dice) {
        this.Dice = Dice;
    }

    public Yahtzee_Display1 getYahtzee_display1() {
        return yahtzee_display1;
    }

    public void setYahtzee_display1(Yahtzee_Display1 yahtzee_display1) {
        this.yahtzee_display1 = yahtzee_display1;
    }

}