





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None doubleButton;
    private None splitButton;
    private None hitButton;
    private boolean showStrategy;
    private None dealButton;
    private None bet;
    private None standButton;



    public GameView(
        None doubleButton,        None splitButton,        None hitButton,        boolean showStrategy,        None dealButton,        None bet,        None standButton    ) {
        this.doubleButton = doubleButton;
        this.splitButton = splitButton;
        this.hitButton = hitButton;
        this.showStrategy = showStrategy;
        this.dealButton = dealButton;
        this.bet = bet;
        this.standButton = standButton;
    }


    public None getDoublebutton() {
        return doubleButton;
    }

    public void setDoublebutton(None doubleButton) {
        this.doubleButton = doubleButton;
    }
    public None getSplitbutton() {
        return splitButton;
    }

    public void setSplitbutton(None splitButton) {
        this.splitButton = splitButton;
    }
    public None getHitbutton() {
        return hitButton;
    }

    public void setHitbutton(None hitButton) {
        this.hitButton = hitButton;
    }
    public boolean getShowstrategy() {
        return showStrategy;
    }

    public void setShowstrategy(boolean showStrategy) {
        this.showStrategy = showStrategy;
    }
    public None getDealbutton() {
        return dealButton;
    }

    public void setDealbutton(None dealButton) {
        this.dealButton = dealButton;
    }
    public None getBet() {
        return bet;
    }

    public void setBet(None bet) {
        this.bet = bet;
    }
    public None getStandbutton() {
        return standButton;
    }

    public void setStandbutton(None standButton) {
        this.standButton = standButton;
    }


}