





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private boolean showStrategy;
    private None dealButton;
    private None hitButton;
    private None standButton;
    private None bet;
    private None splitButton;
    private None doubleButton;



    public GameView(
        boolean showStrategy,        None dealButton,        None hitButton,        None standButton,        None bet,        None splitButton,        None doubleButton    ) {
        this.showStrategy = showStrategy;
        this.dealButton = dealButton;
        this.hitButton = hitButton;
        this.standButton = standButton;
        this.bet = bet;
        this.splitButton = splitButton;
        this.doubleButton = doubleButton;
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
    public None getHitbutton() {
        return hitButton;
    }

    public void setHitbutton(None hitButton) {
        this.hitButton = hitButton;
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
    public None getSplitbutton() {
        return splitButton;
    }

    public void setSplitbutton(None splitButton) {
        this.splitButton = splitButton;
    }
    public None getDoublebutton() {
        return doubleButton;
    }

    public void setDoublebutton(None doubleButton) {
        this.doubleButton = doubleButton;
    }


}