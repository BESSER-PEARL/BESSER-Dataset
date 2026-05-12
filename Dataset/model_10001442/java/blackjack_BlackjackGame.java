





import java.util.List;
import java.util.ArrayList;

public class blackjack_BlackjackGame  {

    private String dealersHandTextView;
    private String playersHandTextView;
    private String stayButton;
    private int MAX_HITS;
    private String hitButton;
    private int MAX_CARDS_PULLED;
    private String dealersHandValueTextView;
    private None gstate;
    private String playerHandValueTextView;
    private String gameResultTextView;



    public blackjack_BlackjackGame(
        String dealersHandTextView,        String playersHandTextView,        String stayButton,        int MAX_HITS,        String hitButton,        int MAX_CARDS_PULLED,        String dealersHandValueTextView,        None gstate,        String playerHandValueTextView,        String gameResultTextView    ) {
        this.dealersHandTextView = dealersHandTextView;
        this.playersHandTextView = playersHandTextView;
        this.stayButton = stayButton;
        this.MAX_HITS = MAX_HITS;
        this.hitButton = hitButton;
        this.MAX_CARDS_PULLED = MAX_CARDS_PULLED;
        this.dealersHandValueTextView = dealersHandValueTextView;
        this.gstate = gstate;
        this.playerHandValueTextView = playerHandValueTextView;
        this.gameResultTextView = gameResultTextView;
    }


    public String getDealershandtextview() {
        return dealersHandTextView;
    }

    public void setDealershandtextview(String dealersHandTextView) {
        this.dealersHandTextView = dealersHandTextView;
    }
    public String getPlayershandtextview() {
        return playersHandTextView;
    }

    public void setPlayershandtextview(String playersHandTextView) {
        this.playersHandTextView = playersHandTextView;
    }
    public String getStaybutton() {
        return stayButton;
    }

    public void setStaybutton(String stayButton) {
        this.stayButton = stayButton;
    }
    public int getMax_hits() {
        return MAX_HITS;
    }

    public void setMax_hits(int MAX_HITS) {
        this.MAX_HITS = MAX_HITS;
    }
    public String getHitbutton() {
        return hitButton;
    }

    public void setHitbutton(String hitButton) {
        this.hitButton = hitButton;
    }
    public int getMax_cards_pulled() {
        return MAX_CARDS_PULLED;
    }

    public void setMax_cards_pulled(int MAX_CARDS_PULLED) {
        this.MAX_CARDS_PULLED = MAX_CARDS_PULLED;
    }
    public String getDealershandvaluetextview() {
        return dealersHandValueTextView;
    }

    public void setDealershandvaluetextview(String dealersHandValueTextView) {
        this.dealersHandValueTextView = dealersHandValueTextView;
    }
    public None getGstate() {
        return gstate;
    }

    public void setGstate(None gstate) {
        this.gstate = gstate;
    }
    public String getPlayerhandvaluetextview() {
        return playerHandValueTextView;
    }

    public void setPlayerhandvaluetextview(String playerHandValueTextView) {
        this.playerHandValueTextView = playerHandValueTextView;
    }
    public String getGameresulttextview() {
        return gameResultTextView;
    }

    public void setGameresulttextview(String gameResultTextView) {
        this.gameResultTextView = gameResultTextView;
    }


}