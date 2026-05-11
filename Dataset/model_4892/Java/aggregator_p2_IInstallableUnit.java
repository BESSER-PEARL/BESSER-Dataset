





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IInstallableUnit  {

    private String filter;
    private boolean singleton;
    private String version;
    private boolean resolved;
    private String id;



    public aggregator_p2_IInstallableUnit(
        String filter,        boolean singleton,        String version,        boolean resolved,        String id    ) {
        this.filter = filter;
        this.singleton = singleton;
        this.version = version;
        this.resolved = resolved;
        this.id = id;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}