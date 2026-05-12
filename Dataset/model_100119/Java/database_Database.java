





import java.util.List;
import java.util.ArrayList;

public class database_Database extends RefDatabase {

    private String name;





    private List<database_RefTable> database_reftables;


    public database_Database(
        String name    ) {
        super(
        );
        this.name = name;
        this.database_reftables = new ArrayList<>();
    }

    public database_Database(
        String name        ArrayList<database_RefTable> database_reftables    ) {
        this.name = name;
        this.database_reftables = database_reftables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<database_RefTable> getDatabase_reftables() {
        return database_reftables;
    }

    public void addDatabase_reftable(Database_reftable database_reftable) {
        this.database_reftables.add(database_reftable);
    }

}