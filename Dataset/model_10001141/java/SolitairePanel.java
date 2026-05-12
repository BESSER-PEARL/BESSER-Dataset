





import java.util.List;
import java.util.ArrayList;

public class SolitairePanel  {

    private String background;
    private String backGroundNumber;



    public SolitairePanel(
        String background,        String backGroundNumber    ) {
        this.background = background;
        this.backGroundNumber = backGroundNumber;
    }


    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getBackgroundnumber() {
        return backGroundNumber;
    }

    public void setBackgroundnumber(String backGroundNumber) {
        this.backGroundNumber = backGroundNumber;
    }


}