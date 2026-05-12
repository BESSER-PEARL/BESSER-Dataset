





import java.util.List;
import java.util.ArrayList;

public class Warehouse  {

    private String database;
    private String location;





    private List<Piece> pieces;


    public Warehouse(
        String database,        String location    ) {
        this.database = database;
        this.location = location;
        this.pieces = new ArrayList<>();
    }

    public Warehouse(
        String database,        String location        ArrayList<Piece> pieces    ) {
        this.database = database;
        this.location = location;
        this.pieces = pieces;
    }

    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<Piece> getPieces() {
        return pieces;
    }

    public void addPiece(Piece piece) {
        this.pieces.add(piece);
    }

}