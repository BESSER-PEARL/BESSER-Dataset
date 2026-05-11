





import java.util.List;
import java.util.ArrayList;

public class roc_FullDirectedAction  {

    private String turnEyes;
    private String turnHead;



    public roc_FullDirectedAction(
        String turnEyes,        String turnHead    ) {
        this.turnEyes = turnEyes;
        this.turnHead = turnHead;
    }


    public String getTurneyes() {
        return turnEyes;
    }

    public void setTurneyes(String turnEyes) {
        this.turnEyes = turnEyes;
    }
    public String getTurnhead() {
        return turnHead;
    }

    public void setTurnhead(String turnHead) {
        this.turnHead = turnHead;
    }


}