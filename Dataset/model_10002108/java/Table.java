





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private None scoreSheet;
    private None Games_6___;
    private None players_5_;
    private int numOfGames;
    private None dealer;





    private Game game;


    public Table(
        None scoreSheet,        None Games_6___,        None players_5_,        int numOfGames,        None dealer    ) {
        this.scoreSheet = scoreSheet;
        this.Games_6___ = Games_6___;
        this.players_5_ = players_5_;
        this.numOfGames = numOfGames;
        this.dealer = dealer;
    }


    public None getScoresheet() {
        return scoreSheet;
    }

    public void setScoresheet(None scoreSheet) {
        this.scoreSheet = scoreSheet;
    }
    public None getGames_6___() {
        return Games_6___;
    }

    public void setGames_6___(None Games_6___) {
        this.Games_6___ = Games_6___;
    }
    public None getPlayers_5_() {
        return players_5_;
    }

    public void setPlayers_5_(None players_5_) {
        this.players_5_ = players_5_;
    }
    public int getNumofgames() {
        return numOfGames;
    }

    public void setNumofgames(int numOfGames) {
        this.numOfGames = numOfGames;
    }
    public None getDealer() {
        return dealer;
    }

    public void setDealer(None dealer) {
        this.dealer = dealer;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

}