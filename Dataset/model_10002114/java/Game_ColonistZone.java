





import java.util.List;
import java.util.ArrayList;

public class Game_ColonistZone  {

    private int MaxColonists;
    private boolean Stackable;
    private None Pieces;



    public Game_ColonistZone(
        int MaxColonists,        boolean Stackable,        None Pieces    ) {
        this.MaxColonists = MaxColonists;
        this.Stackable = Stackable;
        this.Pieces = Pieces;
    }


    public int getMaxcolonists() {
        return MaxColonists;
    }

    public void setMaxcolonists(int MaxColonists) {
        this.MaxColonists = MaxColonists;
    }
    public boolean getStackable() {
        return Stackable;
    }

    public void setStackable(boolean Stackable) {
        this.Stackable = Stackable;
    }
    public None getPieces() {
        return Pieces;
    }

    public void setPieces(None Pieces) {
        this.Pieces = Pieces;
    }


}