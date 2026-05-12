





import java.util.List;
import java.util.ArrayList;

public class Game_GoodZone  {

    private None Pieces;
    private boolean Stackable;



    public Game_GoodZone(
        None Pieces,        boolean Stackable    ) {
        this.Pieces = Pieces;
        this.Stackable = Stackable;
    }


    public None getPieces() {
        return Pieces;
    }

    public void setPieces(None Pieces) {
        this.Pieces = Pieces;
    }
    public boolean getStackable() {
        return Stackable;
    }

    public void setStackable(boolean Stackable) {
        this.Stackable = Stackable;
    }


}