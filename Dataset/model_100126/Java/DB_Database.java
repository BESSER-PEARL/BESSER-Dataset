





import java.util.List;
import java.util.ArrayList;

public class DB_Database  {






    private DB_DatabaseElement db_databaseelement;




    private List<DB_DatabaseElement> db_databaseelements;


    public DB_Database(
    ) {
        this.db_databaseelements = new ArrayList<>();
    }

    public DB_Database(
        ArrayList<DB_DatabaseElement> db_databaseelements    ) {
        this.db_databaseelements = db_databaseelements;
    }


    public DB_DatabaseElement getDb_databaseelement() {
        return db_databaseelement;
    }

    public void setDb_databaseelement(DB_DatabaseElement db_databaseelement) {
        this.db_databaseelement = db_databaseelement;
    }
    public List<DB_DatabaseElement> getDb_databaseelements() {
        return db_databaseelements;
    }

    public void addDb_databaseelement(Db_databaseelement db_databaseelement) {
        this.db_databaseelements.add(db_databaseelement);
    }

}