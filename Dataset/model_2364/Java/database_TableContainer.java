





import java.util.List;
import java.util.ArrayList;

public class database_TableContainer extends NamedElement {






    private List<database_AbstractTable> database_abstracttables;




    private database_AbstractTable database_abstracttable;


    public database_TableContainer(
    ) {
        super(
        );
        this.database_abstracttables = new ArrayList<>();
    }

    public database_TableContainer(
        ArrayList<database_AbstractTable> database_abstracttables    ) {
        this.database_abstracttables = database_abstracttables;
    }


    public List<database_AbstractTable> getDatabase_abstracttables() {
        return database_abstracttables;
    }

    public void addDatabase_abstracttable(Database_abstracttable database_abstracttable) {
        this.database_abstracttables.add(database_abstracttable);
    }
    public database_AbstractTable getDatabase_abstracttable() {
        return database_abstracttable;
    }

    public void setDatabase_abstracttable(database_AbstractTable database_abstracttable) {
        this.database_abstracttable = database_abstracttable;
    }

}