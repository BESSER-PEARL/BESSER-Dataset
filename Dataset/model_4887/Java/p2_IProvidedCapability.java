





import java.util.List;
import java.util.ArrayList;

public class p2_IProvidedCapability  {

    private String name;
    private String version;
    private String namespace;





    private p2_IInstallableUnit p2_iinstallableunit;


    public p2_IProvidedCapability(
        String name,        String version,        String namespace    ) {
        this.name = name;
        this.version = version;
        this.namespace = namespace;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public p2_IInstallableUnit getP2_iinstallableunit() {
        return p2_iinstallableunit;
    }

    public void setP2_iinstallableunit(p2_IInstallableUnit p2_iinstallableunit) {
        this.p2_iinstallableunit = p2_iinstallableunit;
    }

}