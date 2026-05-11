





import java.util.List;
import java.util.ArrayList;

public class model_physical_PhysicalModel extends ModelObject {

    private String databaseVersion;
    private String catalog;
    private String schema;
    private String databaseName;



    public model_physical_PhysicalModel(
        String databaseVersion,        String catalog,        String schema,        String databaseName    ) {
        super(
        );
        this.databaseVersion = databaseVersion;
        this.catalog = catalog;
        this.schema = schema;
        this.databaseName = databaseName;
    }


    public String getDatabaseversion() {
        return databaseVersion;
    }

    public void setDatabaseversion(String databaseVersion) {
        this.databaseVersion = databaseVersion;
    }
    public String getCatalog() {
        return catalog;
    }

    public void setCatalog(String catalog) {
        this.catalog = catalog;
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


}