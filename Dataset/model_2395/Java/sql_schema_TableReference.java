





import java.util.List;
import java.util.ArrayList;

public class sql_schema_TableReference  {

    private String schemaName;
    private String catalogName;





    private TableDefinition tabledefinition;


    public sql_schema_TableReference(
        String schemaName,        String catalogName    ) {
        this.schemaName = schemaName;
        this.catalogName = catalogName;
    }


    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }
    public String getCatalogname() {
        return catalogName;
    }

    public void setCatalogname(String catalogName) {
        this.catalogName = catalogName;
    }

    public TableDefinition getTabledefinition() {
        return tabledefinition;
    }

    public void setTabledefinition(TableDefinition tabledefinition) {
        this.tabledefinition = tabledefinition;
    }

}