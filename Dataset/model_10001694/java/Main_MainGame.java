





import java.util.List;
import java.util.ArrayList;

public class Main_MainGame  {

    private int HighestBid;
    private None screen;
    private int SmallBlind;
    private int Bigblind;
    private int Dealer;
    private String Players;





    private Game_GUI game_gui;


    public Main_MainGame(
        int HighestBid,        None screen,        int SmallBlind,        int Bigblind,        int Dealer,        String Players    ) {
        this.HighestBid = HighestBid;
        this.screen = screen;
        this.SmallBlind = SmallBlind;
        this.Bigblind = Bigblind;
        this.Dealer = Dealer;
        this.Players = Players;
    }


    public int getHighestbid() {
        return HighestBid;
    }

    public void setHighestbid(int HighestBid) {
        this.HighestBid = HighestBid;
    }
    public None getScreen() {
        return screen;
    }

    public void setScreen(None screen) {
        this.screen = screen;
    }
    public int getSmallblind() {
        return SmallBlind;
    }

    public void setSmallblind(int SmallBlind) {
        this.SmallBlind = SmallBlind;
    }
    public int getBigblind() {
        return Bigblind;
    }

    public void setBigblind(int Bigblind) {
        this.Bigblind = Bigblind;
    }
    public int getDealer() {
        return Dealer;
    }

    public void setDealer(int Dealer) {
        this.Dealer = Dealer;
    }
    public String getPlayers() {
        return Players;
    }

    public void setPlayers(String Players) {
        this.Players = Players;
    }

    public Game_GUI getGame_gui() {
        return game_gui;
    }

    public void setGame_gui(Game_GUI game_gui) {
        this.game_gui = game_gui;
    }

}