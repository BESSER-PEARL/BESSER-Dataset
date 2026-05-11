





import java.util.List;
import java.util.ArrayList;

public class migration_Instance  {

    private String uri;
    private String uuid;





    private migration_ModelResource migration_modelresource;


    public migration_Instance(
        String uri,        String uuid    ) {
        this.uri = uri;
        this.uuid = uuid;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public migration_ModelResource getMigration_modelresource() {
        return migration_modelresource;
    }

    public void setMigration_modelresource(migration_ModelResource migration_modelresource) {
        this.migration_modelresource = migration_modelresource;
    }

}