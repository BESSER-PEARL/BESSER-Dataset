





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_SetConnectionStatement extends DefinitionStatement {

    private String databaseName;



    public syntax_ddl_SetConnectionStatement(
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