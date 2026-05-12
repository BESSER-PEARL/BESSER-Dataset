





import java.util.List;
import java.util.ArrayList;

public class GameView  {

    private boolean showStrategy;
    private None bet;
    private None splitButton;
    private None doubleButton;
    private None standButton;
    private None hitButton;
    private None dealButton;



    public GameView(
        boolean showStrategy,        None bet,        None splitButton,        None doubleButton,        None standButton,        None hitButton,        None dealButton    ) {
        this.showStrategy = showStrategy;
        this.bet = bet;
        this.splitButton = splitButton;
        this.doubleButton = doubleButton;
        this.standButton = standButton;
        this.hitButton = hitButton;
        this.dealButton = dealButton;
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
    public None getStandbutton() {
        return standButton;
    }

    public void setStandbutton(None standButton) {
        this.standButton = standButton;
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


}