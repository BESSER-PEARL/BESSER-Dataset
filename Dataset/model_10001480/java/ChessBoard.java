





import java.util.List;
import java.util.ArrayList;

public class ChessBoard  {






    private List<Piece> pieces;


    public ChessBoard(
    ) {
        this.pieces = new ArrayList<>();
    }

    public ChessBoard(
        ArrayList<Piece> pieces    ) {
        this.pieces = pieces;
    }


    public List<Piece> getPieces() {
        return pieces;
    }

    public void addPiece(Piece piece) {
        this.pieces.add(piece);
    }

}