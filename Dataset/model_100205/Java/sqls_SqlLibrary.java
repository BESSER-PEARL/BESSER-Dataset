





import java.util.List;
import java.util.ArrayList;

public class sqls_SqlLibrary  {

    private String database;
    private int version;



    public sqls_SqlLibrary(
        String database,        int version    ) {
        this.database = database;
        this.version = version;
    }


    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }
    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }


}