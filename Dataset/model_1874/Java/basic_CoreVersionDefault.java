





import java.util.List;
import java.util.ArrayList;

public class basic_CoreVersionDefault  {

    private String facet;
    private String coreLib;
    private String version;



    public basic_CoreVersionDefault(
        String facet,        String coreLib,        String version    ) {
        this.facet = facet;
        this.coreLib = coreLib;
        this.version = version;
    }


    public String getFacet() {
        return facet;
    }

    public void setFacet(String facet) {
        this.facet = facet;
    }
    public String getCorelib() {
        return coreLib;
    }

    public void setCorelib(String coreLib) {
        this.coreLib = coreLib;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}