





import java.util.List;
import java.util.ArrayList;

public class Round  {

    private None trick;
    private None RoundStarter;
    private int roundNum;
    private None turnToPlay;





    private Game game;


    public Round(
        None trick,        None RoundStarter,        int roundNum,        None turnToPlay    ) {
        this.trick = trick;
        this.RoundStarter = RoundStarter;
        this.roundNum = roundNum;
        this.turnToPlay = turnToPlay;
    }


    public None getTrick() {
        return trick;
    }

    public void setTrick(None trick) {
        this.trick = trick;
    }
    public None getRoundstarter() {
        return RoundStarter;
    }

    public void setRoundstarter(None RoundStarter) {
        this.RoundStarter = RoundStarter;
    }
    public int getRoundnum() {
        return roundNum;
    }

    public void setRoundnum(int roundNum) {
        this.roundNum = roundNum;
    }
    public None getTurntoplay() {
        return turnToPlay;
    }

    public void setTurntoplay(None turnToPlay) {
        this.turnToPlay = turnToPlay;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

}