





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None standButton;
    private None splitButton;
    private None hitButton;
    private None bet;
    private None dealButton;
    private boolean showStrategy;
    private None doubleButton;



    public GameView(
        None standButton,        None splitButton,        None hitButton,        None bet,        None dealButton,        boolean showStrategy,        None doubleButton    ) {
        this.standButton = standButton;
        this.splitButton = splitButton;
        this.hitButton = hitButton;
        this.bet = bet;
        this.dealButton = dealButton;
        this.showStrategy = showStrategy;
        this.doubleButton = doubleButton;
    }


    public None getStandbutton() {
        return standButton;
    }

    public void setStandbutton(None standButton) {
        this.standButton = standButton;
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
    public None getDoublebutton() {
        return doubleButton;
    }

    public void setDoublebutton(None doubleButton) {
        this.doubleButton = doubleButton;
    }


}