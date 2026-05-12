





import java.util.List;
import java.util.ArrayList;

public class Piece  {

    private String pieceColor;
    private int pieceSize;



    public Piece(
        String pieceColor,        int pieceSize    ) {
        this.pieceColor = pieceColor;
        this.pieceSize = pieceSize;
    }


    public String getPiececolor() {
        return pieceColor;
    }

    public void setPiececolor(String pieceColor) {
        this.pieceColor = pieceColor;
    }
    public int getPiecesize() {
        return pieceSize;
    }

    public void setPiecesize(int pieceSize) {
        this.pieceSize = pieceSize;
    }


}