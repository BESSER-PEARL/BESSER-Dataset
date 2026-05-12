





import java.util.List;
import java.util.ArrayList;

public class GameElements  {

    private String WildActions;
    private String CardNumber;
    private String Actions;
    private String CardColors;
    private String CardsTotal;
    private String Action;
    private None Numbers;
    private String WildCardCol;
    private String OpeningHand;
    private String Wild;



    public GameElements(
        String WildActions,        String CardNumber,        String Actions,        String CardColors,        String CardsTotal,        String Action,        None Numbers,        String WildCardCol,        String OpeningHand,        String Wild    ) {
        this.WildActions = WildActions;
        this.CardNumber = CardNumber;
        this.Actions = Actions;
        this.CardColors = CardColors;
        this.CardsTotal = CardsTotal;
        this.Action = Action;
        this.Numbers = Numbers;
        this.WildCardCol = WildCardCol;
        this.OpeningHand = OpeningHand;
        this.Wild = Wild;
    }


    public String getWildactions() {
        return WildActions;
    }

    public void setWildactions(String WildActions) {
        this.WildActions = WildActions;
    }
    public String getCardnumber() {
        return CardNumber;
    }

    public void setCardnumber(String CardNumber) {
        this.CardNumber = CardNumber;
    }
    public String getActions() {
        return Actions;
    }

    public void setActions(String Actions) {
        this.Actions = Actions;
    }
    public String getCardcolors() {
        return CardColors;
    }

    public void setCardcolors(String CardColors) {
        this.CardColors = CardColors;
    }
    public String getCardstotal() {
        return CardsTotal;
    }

    public void setCardstotal(String CardsTotal) {
        this.CardsTotal = CardsTotal;
    }
    public String getAction() {
        return Action;
    }

    public void setAction(String Action) {
        this.Action = Action;
    }
    public None getNumbers() {
        return Numbers;
    }

    public void setNumbers(None Numbers) {
        this.Numbers = Numbers;
    }
    public String getWildcardcol() {
        return WildCardCol;
    }

    public void setWildcardcol(String WildCardCol) {
        this.WildCardCol = WildCardCol;
    }
    public String getOpeninghand() {
        return OpeningHand;
    }

    public void setOpeninghand(String OpeningHand) {
        this.OpeningHand = OpeningHand;
    }
    public String getWild() {
        return Wild;
    }

    public void setWild(String Wild) {
        this.Wild = Wild;
    }


}