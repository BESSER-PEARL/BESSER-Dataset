





import java.util.List;
import java.util.ArrayList;

public class Spot  {

    private int x;
    private int y;
    private None piece;



    public Spot(
        int x,        int y,        None piece    ) {
        this.x = x;
        this.y = y;
        this.piece = piece;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public None getPiece() {
        return piece;
    }

    public void setPiece(None piece) {
        this.piece = piece;
    }


}