





import java.util.List;
import java.util.ArrayList;

public class sql_common_SchemaQualifiedName  {

    private String schemaName;
    private String name;
    private String catalogName;



    public sql_common_SchemaQualifiedName(
        String schemaName,        String name,        String catalogName    ) {
        this.schemaName = schemaName;
        this.name = name;
        this.catalogName = catalogName;
    }


    public String getSchemaname() {
        return schemaName;
    }

    public void setSchemaname(String schemaName) {
        this.schemaName = schemaName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCatalogname() {
        return catalogName;
    }

    public void setCatalogname(String catalogName) {
        this.catalogName = catalogName;
    }


}