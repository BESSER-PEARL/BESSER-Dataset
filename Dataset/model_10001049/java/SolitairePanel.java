





import java.util.List;
import java.util.ArrayList;

public class SolitairePanel  {

    private int backgroundNumber;
    private String background;





    private SolitaireBoard solitaireboard;


    public SolitairePanel(
        int backgroundNumber,        String background    ) {
        this.backgroundNumber = backgroundNumber;
        this.background = background;
    }


    public int getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(int backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }

    public SolitaireBoard getSolitaireboard() {
        return solitaireboard;
    }

    public void setSolitaireboard(SolitaireBoard solitaireboard) {
        this.solitaireboard = solitaireboard;
    }

}