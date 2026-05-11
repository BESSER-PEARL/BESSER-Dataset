





import java.util.List;
import java.util.ArrayList;

public class relationaldb_Table extends Named {






    private List<relationaldb_Column> relationaldb_columns;




    private List<relationaldb_Column> relationaldb_columns;




    private relationaldb_Column relationaldb_column;




    private relationaldb_Database relationaldb_database;


    public relationaldb_Table(
    ) {
        super(
        );
        this.relationaldb_columns = new ArrayList<>();
        this.relationaldb_columns = new ArrayList<>();
    }

    public relationaldb_Table(
        ArrayList<relationaldb_Column> relationaldb_columns,        ArrayList<relationaldb_Column> relationaldb_columns    ) {
        this.relationaldb_columns = relationaldb_columns;
        this.relationaldb_columns = relationaldb_columns;
    }


    public List<relationaldb_Column> getRelationaldb_columns() {
        return relationaldb_columns;
    }

    public void addRelationaldb_column(Relationaldb_column relationaldb_column) {
        this.relationaldb_columns.add(relationaldb_column);
    }
    public List<relationaldb_Column> getRelationaldb_columns() {
        return relationaldb_columns;
    }

    public void addRelationaldb_column(Relationaldb_column relationaldb_column) {
        this.relationaldb_columns.add(relationaldb_column);
    }
    public relationaldb_Column getRelationaldb_column() {
        return relationaldb_column;
    }

    public void setRelationaldb_column(relationaldb_Column relationaldb_column) {
        this.relationaldb_column = relationaldb_column;
    }
    public relationaldb_Database getRelationaldb_database() {
        return relationaldb_database;
    }

    public void setRelationaldb_database(relationaldb_Database relationaldb_database) {
        this.relationaldb_database = relationaldb_database;
    }

}