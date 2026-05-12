





import java.util.List;
import java.util.ArrayList;

public class Board  {

    private String playAagain;
    private String cardArea;



    public Board(
        String playAagain,        String cardArea    ) {
        this.playAagain = playAagain;
        this.cardArea = cardArea;
    }


    public String getPlayaagain() {
        return playAagain;
    }

    public void setPlayaagain(String playAagain) {
        this.playAagain = playAagain;
    }
    public String getCardarea() {
        return cardArea;
    }

    public void setCardarea(String cardArea) {
        this.cardArea = cardArea;
    }


}