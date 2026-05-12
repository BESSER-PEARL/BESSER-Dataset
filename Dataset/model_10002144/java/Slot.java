





import java.util.List;
import java.util.ArrayList;

public class Slot  {

    private None piece;
    private boolean Occupied;



    public Slot(
        None piece,        boolean Occupied    ) {
        this.piece = piece;
        this.Occupied = Occupied;
    }


    public None getPiece() {
        return piece;
    }

    public void setPiece(None piece) {
        this.piece = piece;
    }
    public boolean getOccupied() {
        return Occupied;
    }

    public void setOccupied(boolean Occupied) {
        this.Occupied = Occupied;
    }


}