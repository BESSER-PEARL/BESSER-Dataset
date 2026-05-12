





import java.util.List;
import java.util.ArrayList;

public class Square  {

    private None position;
    private None piece;



    public Square(
        None position,        None piece    ) {
        this.position = position;
        this.piece = piece;
    }


    public None getPosition() {
        return position;
    }

    public void setPosition(None position) {
        this.position = position;
    }
    public None getPiece() {
        return piece;
    }

    public void setPiece(None piece) {
        this.piece = piece;
    }


}