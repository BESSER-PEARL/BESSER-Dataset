





import java.util.List;
import java.util.ArrayList;

public class p2_ITouchpointType  {

    private String id;
    private String version;





    private p2_IInstallableUnit p2_iinstallableunit;


    public p2_ITouchpointType(
        String id,        String version    ) {
        this.id = id;
        this.version = version;
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

    public p2_IInstallableUnit getP2_iinstallableunit() {
        return p2_iinstallableunit;
    }

    public void setP2_iinstallableunit(p2_IInstallableUnit p2_iinstallableunit) {
        this.p2_iinstallableunit = p2_iinstallableunit;
    }

}