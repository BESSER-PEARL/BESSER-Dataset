





import java.util.List;
import java.util.ArrayList;

public class database_TableContainer extends NamedElement {






    private database_AbstractTable database_abstracttable;




    private List<database_Sequence> database_sequences;




    private List<database_AbstractTable> database_abstracttables;


    public database_TableContainer(
    ) {
        super(
        );
        this.database_sequences = new ArrayList<>();
        this.database_abstracttables = new ArrayList<>();
    }

    public database_TableContainer(
        ArrayList<database_Sequence> database_sequences,        ArrayList<database_AbstractTable> database_abstracttables    ) {
        this.database_sequences = database_sequences;
        this.database_abstracttables = database_abstracttables;
    }


    public database_AbstractTable getDatabase_abstracttable() {
        return database_abstracttable;
    }

    public void setDatabase_abstracttable(database_AbstractTable database_abstracttable) {
        this.database_abstracttable = database_abstracttable;
    }
    public List<database_Sequence> getDatabase_sequences() {
        return database_sequences;
    }

    public void addDatabase_sequence(Database_sequence database_sequence) {
        this.database_sequences.add(database_sequence);
    }
    public List<database_AbstractTable> getDatabase_abstracttables() {
        return database_abstracttables;
    }

    public void addDatabase_abstracttable(Database_abstracttable database_abstracttable) {
        this.database_abstracttables.add(database_abstracttable);
    }

}