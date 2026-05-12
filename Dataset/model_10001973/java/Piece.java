





import java.util.List;
import java.util.ArrayList;

public class Piece  {

    private int pieceSize;
    private String pieceColor;



    public Piece(
        int pieceSize,        String pieceColor    ) {
        this.pieceSize = pieceSize;
        this.pieceColor = pieceColor;
    }


    public int getPiecesize() {
        return pieceSize;
    }

    public void setPiecesize(int pieceSize) {
        this.pieceSize = pieceSize;
    }
    public String getPiececolor() {
        return pieceColor;
    }

    public void setPiececolor(String pieceColor) {
        this.pieceColor = pieceColor;
    }


}