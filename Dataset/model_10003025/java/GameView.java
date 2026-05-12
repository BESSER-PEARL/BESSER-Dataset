





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None hitButton;
    private None dealButton;
    private boolean showStrategy;
    private None splitButton;
    private None standButton;
    private None bet;
    private None doubleButton;



    public GameView(
        None hitButton,        None dealButton,        boolean showStrategy,        None splitButton,        None standButton,        None bet,        None doubleButton    ) {
        this.hitButton = hitButton;
        this.dealButton = dealButton;
        this.showStrategy = showStrategy;
        this.splitButton = splitButton;
        this.standButton = standButton;
        this.bet = bet;
        this.doubleButton = doubleButton;
    }


    public None getHitbutton() {
        return hitButton;
    }

    public void setHitbutton(None hitButton) {
        this.hitButton = hitButton;
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
    public None getSplitbutton() {
        return splitButton;
    }

    public void setSplitbutton(None splitButton) {
        this.splitButton = splitButton;
    }
    public None getStandbutton() {
        return standButton;
    }

    public void setStandbutton(None standButton) {
        this.standButton = standButton;
    }
    public None getBet() {
        return bet;
    }

    public void setBet(None bet) {
        this.bet = bet;
    }
    public None getDoublebutton() {
        return doubleButton;
    }

    public void setDoublebutton(None doubleButton) {
        this.doubleButton = doubleButton;
    }


}