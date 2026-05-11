





import java.util.List;
import java.util.ArrayList;

public class sql_common_SchemaQualifiedName  {

    private String name;
    private String schemaName;
    private String catalogName;



    public sql_common_SchemaQualifiedName(
        String name,        String schemaName,        String catalogName    ) {
        this.name = name;
        this.schemaName = schemaName;
        this.catalogName = catalogName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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


}