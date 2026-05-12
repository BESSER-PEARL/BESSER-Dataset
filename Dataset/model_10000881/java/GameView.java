





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None bet;
    private None dealButton;
    private boolean showStrategy;
    private None standButton;
    private None doubleButton;
    private None splitButton;
    private None hitButton;



    public GameView(
        None bet,        None dealButton,        boolean showStrategy,        None standButton,        None doubleButton,        None splitButton,        None hitButton    ) {
        this.bet = bet;
        this.dealButton = dealButton;
        this.showStrategy = showStrategy;
        this.standButton = standButton;
        this.doubleButton = doubleButton;
        this.splitButton = splitButton;
        this.hitButton = hitButton;
    }


    public None getBet() {
        return bet;
    }

    public void setBet(None bet) {
        this.bet = bet;
    }
    public None getDealbutton() {
        return dealButton;
    }

    public void setDealbutton(None dealButton) {
        this.dealButton = dealButton;
    }
    public boolean getShowstrategy() {
        return showStrategy;
    }

    public void setShowstrategy(boolean showStrategy) {
        this.showStrategy = showStrategy;
    }
    public None getStandbutton() {
        return standButton;
    }

    public void setStandbutton(None standButton) {
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


}