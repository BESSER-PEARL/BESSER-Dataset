





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IInstallableUnit  {

    private String version;
    private String filter;
    private String id;
    private boolean resolved;
    private boolean singleton;





    private ITouchpointType itouchpointtype;


    public aggregator_p2_IInstallableUnit(
        String version,        String filter,        String id,        boolean resolved,        boolean singleton    ) {
        this.version = version;
        this.filter = filter;
        this.id = id;
        this.resolved = resolved;
        this.singleton = singleton;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }

    public ITouchpointType getItouchpointtype() {
        return itouchpointtype;
    }

    public void setItouchpointtype(ITouchpointType itouchpointtype) {
        this.itouchpointtype = itouchpointtype;
    }

}