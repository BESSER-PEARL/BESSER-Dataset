





import java.util.List;
import java.util.ArrayList;

public class p2_LocationType  {

    private String includeConfigurePhase;
    private String includeAllPlatforms;
    private String includeSource;
    private String type;
    private String includeMode;





    private p2_LocationsType p2_locationstype;


    public p2_LocationType(
        String includeConfigurePhase,        String includeAllPlatforms,        String includeSource,        String type,        String includeMode    ) {
        this.includeConfigurePhase = includeConfigurePhase;
        this.includeAllPlatforms = includeAllPlatforms;
        this.includeSource = includeSource;
        this.type = type;
        this.includeMode = includeMode;
    }


    public String getIncludeconfigurephase() {
        return includeConfigurePhase;
    }

    public void setIncludeconfigurephase(String includeConfigurePhase) {
        this.includeConfigurePhase = includeConfigurePhase;
    }
    public String getIncludeallplatforms() {
        return includeAllPlatforms;
    }

    public void setIncludeallplatforms(String includeAllPlatforms) {
        this.includeAllPlatforms = includeAllPlatforms;
    }
    public String getIncludesource() {
        return includeSource;
    }

    public void setIncludesource(String includeSource) {
        this.includeSource = includeSource;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIncludemode() {
        return includeMode;
    }

    public void setIncludemode(String includeMode) {
        this.includeMode = includeMode;
    }

    public p2_LocationsType getP2_locationstype() {
        return p2_locationstype;
    }

    public void setP2_locationstype(p2_LocationsType p2_locationstype) {
        this.p2_locationstype = p2_locationstype;
    }

}