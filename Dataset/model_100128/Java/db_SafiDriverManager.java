





import java.util.List;
import java.util.ArrayList;

public class db_SafiDriverManager extends DBResource {






    private db_DBDriver db_dbdriver;




    private List<db_DBDriver> db_dbdrivers;


    public db_SafiDriverManager(
    ) {
        super(
        );
        this.db_dbdrivers = new ArrayList<>();
    }

    public db_SafiDriverManager(
        ArrayList<db_DBDriver> db_dbdrivers    ) {
        this.db_dbdrivers = db_dbdrivers;
    }


    public db_DBDriver getDb_dbdriver() {
        return db_dbdriver;
    }

    public void setDb_dbdriver(db_DBDriver db_dbdriver) {
        this.db_dbdriver = db_dbdriver;
    }
    public List<db_DBDriver> getDb_dbdrivers() {
        return db_dbdrivers;
    }

    public void addDb_dbdriver(Db_dbdriver db_dbdriver) {
        this.db_dbdrivers.add(db_dbdriver);
    }

}