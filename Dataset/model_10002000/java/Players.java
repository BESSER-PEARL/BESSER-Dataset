





import java.util.List;
import java.util.ArrayList;

public class Players  {

    private String Player__;
    private String playCard_Card_;
    private String hasCard_Card_;
    private String Players__;
    private String drawCard_Card_;
    private String Player_String_;
    private String getName;



    public Players(
        String Player__,        String playCard_Card_,        String hasCard_Card_,        String Players__,        String drawCard_Card_,        String Player_String_,        String getName    ) {
        this.Player__ = Player__;
        this.playCard_Card_ = playCard_Card_;
        this.hasCard_Card_ = hasCard_Card_;
        this.Players__ = Players__;
        this.drawCard_Card_ = drawCard_Card_;
        this.Player_String_ = Player_String_;
        this.getName = getName;
    }


    public String getPlayer__() {
        return Player__;
    }

    public void setPlayer__(String Player__) {
        this.Player__ = Player__;
    }
    public String getPlaycard_card_() {
        return playCard_Card_;
    }

    public void setPlaycard_card_(String playCard_Card_) {
        this.playCard_Card_ = playCard_Card_;
    }
    public String getHascard_card_() {
        return hasCard_Card_;
    }

    public void setHascard_card_(String hasCard_Card_) {
        this.hasCard_Card_ = hasCard_Card_;
    }
    public String getPlayers__() {
        return Players__;
    }

    public void setPlayers__(String Players__) {
        this.Players__ = Players__;
    }
    public String getDrawcard_card_() {
        return drawCard_Card_;
    }

    public void setDrawcard_card_(String drawCard_Card_) {
        this.drawCard_Card_ = drawCard_Card_;
    }
    public String getPlayer_string_() {
        return Player_String_;
    }

    public void setPlayer_string_(String Player_String_) {
        this.Player_String_ = Player_String_;
    }
    public String getGetname() {
        return getName;
    }

    public void setGetname(String getName) {
        this.getName = getName;
    }


}