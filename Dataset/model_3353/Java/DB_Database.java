





import java.util.List;
import java.util.ArrayList;

public class DB_Database  {

    private String Name;





    private List<DB_Table> db_tables;


    public DB_Database(
        String Name    ) {
        this.Name = Name;
        this.db_tables = new ArrayList<>();
    }

    public DB_Database(
        String Name        ArrayList<DB_Table> db_tables    ) {
        this.Name = Name;
        this.db_tables = db_tables;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<DB_Table> getDb_tables() {
        return db_tables;
    }

    public void addDb_table(Db_table db_table) {
        this.db_tables.add(db_table);
    }

}