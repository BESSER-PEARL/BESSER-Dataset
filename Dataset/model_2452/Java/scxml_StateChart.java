





import java.util.List;
import java.util.ArrayList;

public class scxml_StateChart extends DescriptionContainer, AbstractState, DatamodelContainer, AbstractSimpleState {

    private String profile;
    private String xmlns;
    private String id;
    private String exmode;
    private String version;



    public scxml_StateChart(
        String profile,        String xmlns,        String id,        String exmode,        String version    ) {
        super(
        );
        this.profile = profile;
        this.xmlns = xmlns;
        this.id = id;
        this.exmode = exmode;
        this.version = version;
    }


    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }
    public String getXmlns() {
        return xmlns;
    }

    public void setXmlns(String xmlns) {
        this.xmlns = xmlns;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getExmode() {
        return exmode;
    }

    public void setExmode(String exmode) {
        this.exmode = exmode;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}