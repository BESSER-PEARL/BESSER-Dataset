





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Database extends DataDefinition {

    private String databaseName;



    public DML_DDL_Database(
        String databaseName    ) {
        super(
        );
        this.databaseName = databaseName;
    }


    public String getDatabasename() {
        return databaseName;
    }

    public void setDatabasename(String databaseName) {
        this.databaseName = databaseName;
    }


}