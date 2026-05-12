





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Game  {

    private None CompPlayer;
    private None Player;
    private int First;
    private boolean Again;



    public Yahtzee_Game(
        None CompPlayer,        None Player,        int First,        boolean Again    ) {
        this.CompPlayer = CompPlayer;
        this.Player = Player;
        this.First = First;
        this.Again = Again;
    }


    public None getCompplayer() {
        return CompPlayer;
    }

    public void setCompplayer(None CompPlayer) {
        this.CompPlayer = CompPlayer;
    }
    public None getPlayer() {
        return Player;
    }

    public void setPlayer(None Player) {
        this.Player = Player;
    }
    public int getFirst() {
        return First;
    }

    public void setFirst(int First) {
        this.First = First;
    }
    public boolean getAgain() {
        return Again;
    }

    public void setAgain(boolean Again) {
        this.Again = Again;
    }


}