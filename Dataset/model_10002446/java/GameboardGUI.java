





import java.util.List;
import java.util.ArrayList;

public class GameboardGUI  {

    private String piecesList;
    private int rows;
    private int columns;





    private List<Piece> pieces;


    public GameboardGUI(
        String piecesList,        int rows,        int columns    ) {
        this.piecesList = piecesList;
        this.rows = rows;
        this.columns = columns;
        this.pieces = new ArrayList<>();
    }

    public GameboardGUI(
        String piecesList,        int rows,        int columns        ArrayList<Piece> pieces    ) {
        this.piecesList = piecesList;
        this.rows = rows;
        this.columns = columns;
        this.pieces = pieces;
    }

    public String getPieceslist() {
        return piecesList;
    }

    public void setPieceslist(String piecesList) {
        this.piecesList = piecesList;
    }
    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
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