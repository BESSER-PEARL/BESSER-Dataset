





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IInstallableUnit  {

    private String id;
    private String filter;
    private boolean resolved;
    private String version;
    private boolean singleton;



    public aggregator_p2_IInstallableUnit(
        String id,        String filter,        boolean resolved,        String version,        boolean singleton    ) {
        this.id = id;
        this.filter = filter;
        this.resolved = resolved;
        this.version = version;
        this.singleton = singleton;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }


}