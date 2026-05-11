





import java.util.List;
import java.util.ArrayList;

public class model_physical_PhysicalModel extends ModelObject {

    private String schema;
    private String databaseName;
    private String catalog;
    private String databaseVersion;



    public model_physical_PhysicalModel(
        String schema,        String databaseName,        String catalog,        String databaseVersion    ) {
        super(
        );
        this.schema = schema;
        this.databaseName = databaseName;
        this.catalog = catalog;
        this.databaseVersion = databaseVersion;
    }


    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }
    public String getDatabasename() {
        return databaseName;
    }

    public void setDatabasename(String databaseName) {
        this.databaseName = databaseName;
    }
    public String getCatalog() {
        return catalog;
    }

    public void setCatalog(String catalog) {
        this.catalog = catalog;
    }
    public String getDatabaseversion() {
        return databaseVersion;
    }

    public void setDatabaseversion(String databaseVersion) {
        this.databaseVersion = databaseVersion;
    }


}