





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None standButton;
    private None dealButton;
    private None splitButton;
    private boolean showStrategy;
    private None bet;
    private None hitButton;
    private None doubleButton;



    public GameView(
        None standButton,        None dealButton,        None splitButton,        boolean showStrategy,        None bet,        None hitButton,        None doubleButton    ) {
        this.standButton = standButton;
        this.dealButton = dealButton;
        this.splitButton = splitButton;
        this.showStrategy = showStrategy;
        this.bet = bet;
        this.hitButton = hitButton;
        this.doubleButton = doubleButton;
    }


    public None getStandbutton() {
        return standButton;
    }

    public void setStandbutton(None standButton) {
        this.standButton = standButton;
    }
    public None getDealbutton() {
        return dealButton;
    }

    public void setDealbutton(None dealButton) {
        this.dealButton = dealButton;
    }
    public None getSplitbutton() {
        return splitButton;
    }

    public void setSplitbutton(None splitButton) {
        this.splitButton = splitButton;
    }
    public boolean getShowstrategy() {
        return showStrategy;
    }

    public void setShowstrategy(boolean showStrategy) {
        this.showStrategy = showStrategy;
    }
    public None getBet() {
        return bet;
    }

    public void setBet(None bet) {
        this.bet = bet;
    }
    public None getHitbutton() {
        return hitButton;
    }

    public void setHitbutton(None hitButton) {
        this.hitButton = hitButton;
    }
    public None getDoublebutton() {
        return doubleButton;
    }

    public void setDoublebutton(None doubleButton) {
        this.doubleButton = doubleButton;
    }


}