





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IInstallableUnit  {

    private String version;
    private String id;
    private String filter;
    private boolean singleton;
    private boolean resolved;



    public aggregator_p2_IInstallableUnit(
        String version,        String id,        String filter,        boolean singleton,        boolean resolved    ) {
        this.version = version;
        this.id = id;
        this.filter = filter;
        this.singleton = singleton;
        this.resolved = resolved;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }


}