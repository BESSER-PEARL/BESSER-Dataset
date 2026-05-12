





import java.util.List;
import java.util.ArrayList;

public class BowlingGame  {

    private String attempts;
    private String nextGames;
    private None previousGame;
    private None scoreType;



    public BowlingGame(
        String attempts,        String nextGames,        None previousGame,        None scoreType    ) {
        this.attempts = attempts;
        this.nextGames = nextGames;
        this.previousGame = previousGame;
        this.scoreType = scoreType;
    }


    public String getAttempts() {
        return attempts;
    }

    public void setAttempts(String attempts) {
        this.attempts = attempts;
    }
    public String getNextgames() {
        return nextGames;
    }

    public void setNextgames(String nextGames) {
        this.nextGames = nextGames;
    }
    public None getPreviousgame() {
        return previousGame;
    }

    public void setPreviousgame(None previousGame) {
        this.previousGame = previousGame;
    }
    public None getScoretype() {
        return scoreType;
    }

    public void setScoretype(None scoreType) {
        this.scoreType = scoreType;
    }


}