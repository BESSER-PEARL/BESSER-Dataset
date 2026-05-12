





import java.util.List;
import java.util.ArrayList;

public class Model  {

    private String gameTable;
    private String pl2points;
    private String selected;
    private String pl2;
    private boolean gameOver;
    private String pl1points;
    private String playerNr;
    private String steps;
    private boolean goodselected;
    private String gameSize;
    private String pl1;



    public Model(
        String gameTable,        String pl2points,        String selected,        String pl2,        boolean gameOver,        String pl1points,        String playerNr,        String steps,        boolean goodselected,        String gameSize,        String pl1    ) {
        this.gameTable = gameTable;
        this.pl2points = pl2points;
        this.selected = selected;
        this.pl2 = pl2;
        this.gameOver = gameOver;
        this.pl1points = pl1points;
        this.playerNr = playerNr;
        this.steps = steps;
        this.goodselected = goodselected;
        this.gameSize = gameSize;
        this.pl1 = pl1;
    }


    public String getGametable() {
        return gameTable;
    }

    public void setGametable(String gameTable) {
        this.gameTable = gameTable;
    }
    public String getPl2points() {
        return pl2points;
    }

    public void setPl2points(String pl2points) {
        this.pl2points = pl2points;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }
    public String getPl2() {
        return pl2;
    }

    public void setPl2(String pl2) {
        this.pl2 = pl2;
    }
    public boolean getGameover() {
        return gameOver;
    }

    public void setGameover(boolean gameOver) {
        this.gameOver = gameOver;
    }
    public String getPl1points() {
        return pl1points;
    }

    public void setPl1points(String pl1points) {
        this.pl1points = pl1points;
    }
    public String getPlayernr() {
        return playerNr;
    }

    public void setPlayernr(String playerNr) {
        this.playerNr = playerNr;
    }
    public String getSteps() {
        return steps;
    }

    public void setSteps(String steps) {
        this.steps = steps;
    }
    public boolean getGoodselected() {
        return goodselected;
    }

    public void setGoodselected(boolean goodselected) {
        this.goodselected = goodselected;
    }
    public String getGamesize() {
        return gameSize;
    }

    public void setGamesize(String gameSize) {
        this.gameSize = gameSize;
    }
    public String getPl1() {
        return pl1;
    }

    public void setPl1(String pl1) {
        this.pl1 = pl1;
    }


}