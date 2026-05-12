





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private None doubleButton;
    private boolean showStrategy;
    private None standButton;
    private None bet;
    private None splitButton;
    private None dealButton;
    private None hitButton;



    public GameView(
        None doubleButton,        boolean showStrategy,        None standButton,        None bet,        None splitButton,        None dealButton,        None hitButton    ) {
        this.doubleButton = doubleButton;
        this.showStrategy = showStrategy;
        this.standButton = standButton;
        this.bet = bet;
        this.splitButton = splitButton;
        this.dealButton = dealButton;
        this.hitButton = hitButton;
    }


    public None getDoublebutton() {
        return doubleButton;
    }

    public void setDoublebutton(None doubleButton) {
        this.doubleButton = doubleButton;
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


}