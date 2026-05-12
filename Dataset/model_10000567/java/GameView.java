





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None standButton;
    private None doubleButton;
    private None hitButton;
    private None bet;
    private boolean showStrategy;
    private None splitButton;
    private None dealButton;



    public GameView(
        None standButton,        None doubleButton,        None hitButton,        None bet,        boolean showStrategy,        None splitButton,        None dealButton    ) {
        this.standButton = standButton;
        this.doubleButton = doubleButton;
        this.hitButton = hitButton;
        this.bet = bet;
        this.showStrategy = showStrategy;
        this.splitButton = splitButton;
        this.dealButton = dealButton;
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
    public None getDealbutton() {
        return dealButton;
    }

    public void setDealbutton(None dealButton) {
        this.dealButton = dealButton;
    }


}