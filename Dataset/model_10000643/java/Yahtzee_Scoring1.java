





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Scoring1  {

    private String Temp;





    private Yahtzee_Display1 yahtzee_display1;




    private Yahtzee_Turn1 yahtzee_turn1;


    public Yahtzee_Scoring1(
        String Temp    ) {
        this.Temp = Temp;
    }


    public String getTemp() {
        return Temp;
    }

    public void setTemp(String Temp) {
        this.Temp = Temp;
    }

    public Yahtzee_Display1 getYahtzee_display1() {
        return yahtzee_display1;
    }

    public void setYahtzee_display1(Yahtzee_Display1 yahtzee_display1) {
        this.yahtzee_display1 = yahtzee_display1;
    }
    public Yahtzee_Turn1 getYahtzee_turn1() {
        return yahtzee_turn1;
    }

    public void setYahtzee_turn1(Yahtzee_Turn1 yahtzee_turn1) {
        this.yahtzee_turn1 = yahtzee_turn1;
    }

}