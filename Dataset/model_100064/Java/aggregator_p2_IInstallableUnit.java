





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IInstallableUnit  {

    private String filter;
    private boolean resolved;
    private boolean singleton;
    private String id;
    private String version;





    private ITouchpointType itouchpointtype;


    public aggregator_p2_IInstallableUnit(
        String filter,        boolean resolved,        boolean singleton,        String id,        String version    ) {
        this.filter = filter;
        this.resolved = resolved;
        this.singleton = singleton;
        this.id = id;
        this.version = version;
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
    public boolean getSingleton() {
        return singleton;
    }

    public void setSingleton(boolean singleton) {
        this.singleton = singleton;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public ITouchpointType getItouchpointtype() {
        return itouchpointtype;
    }

    public void setItouchpointtype(ITouchpointType itouchpointtype) {
        this.itouchpointtype = itouchpointtype;
    }

}