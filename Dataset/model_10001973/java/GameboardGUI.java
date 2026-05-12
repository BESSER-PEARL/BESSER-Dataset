





import java.util.List;
import java.util.ArrayList;

public class GameboardGUI  {

    private int rows;
    private String piecesList;
    private int columns;





    private List<Piece> pieces;


    public GameboardGUI(
        int rows,        String piecesList,        int columns    ) {
        this.rows = rows;
        this.piecesList = piecesList;
        this.columns = columns;
        this.pieces = new ArrayList<>();
    }

    public GameboardGUI(
        int rows,        String piecesList,        int columns        ArrayList<Piece> pieces    ) {
        this.rows = rows;
        this.piecesList = piecesList;
        this.columns = columns;
        this.pieces = pieces;
    }

    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }
    public String getPieceslist() {
        return piecesList;
    }

    public void setPieceslist(String piecesList) {
        this.piecesList = piecesList;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }

    public List<Piece> getPieces() {
        return pieces;
    }

    public void addPiece(Piece piece) {
        this.pieces.add(piece);
    }

}