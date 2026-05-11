





import java.util.List;
import java.util.ArrayList;

public class ddsm_ClientNode extends InternalComponent {

    private String type;
    private String artifactUrl;
    private String mainClass;



    public ddsm_ClientNode(
        String type,        String artifactUrl,        String mainClass    ) {
        super(
        );
        this.type = type;
        this.artifactUrl = artifactUrl;
        this.mainClass = mainClass;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getArtifacturl() {
        return artifactUrl;
    }

    public void setArtifacturl(String artifactUrl) {
        this.artifactUrl = artifactUrl;
    }
    public String getMainclass() {
        return mainClass;
    }

    public void setMainclass(String mainClass) {
        this.mainClass = mainClass;
    }


}