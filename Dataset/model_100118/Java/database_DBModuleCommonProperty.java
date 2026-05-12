





import java.util.List;
import java.util.ArrayList;

public class database_DBModuleCommonProperty  {

    private String supportDatabases;
    private String database;



    public database_DBModuleCommonProperty(
        String supportDatabases,        String database    ) {
        this.supportDatabases = supportDatabases;
        this.database = database;
    }


    public String getSupportdatabases() {
        return supportDatabases;
    }

    public void setSupportdatabases(String supportDatabases) {
        this.supportDatabases = supportDatabases;
    }
    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }


}