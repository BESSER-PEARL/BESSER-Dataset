





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Game  {

    private boolean Again;
    private None CompPlayer;
    private int First;
    private None Player;



    public Yahtzee_Game(
        boolean Again,        None CompPlayer,        int First,        None Player    ) {
        this.Again = Again;
        this.CompPlayer = CompPlayer;
        this.First = First;
        this.Player = Player;
    }


    public boolean getAgain() {
        return Again;
    }

    public void setAgain(boolean Again) {
        this.Again = Again;
    }
    public None getCompplayer() {
        return CompPlayer;
    }

    public void setCompplayer(None CompPlayer) {
        this.CompPlayer = CompPlayer;
    }
    public int getFirst() {
        return First;
    }

    public void setFirst(int First) {
        this.First = First;
    }
    public None getPlayer() {
        return Player;
    }

    public void setPlayer(None Player) {
        this.Player = Player;
    }


}