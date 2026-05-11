





import java.util.List;
import java.util.ArrayList;

public class p2_IArtifactKey  {

    private String version;
    private String id;
    private String classifier;





    private p2_ArtifactsByKey p2_artifactsbykey;


    public p2_IArtifactKey(
        String version,        String id,        String classifier    ) {
        this.version = version;
        this.id = id;
        this.classifier = classifier;
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
    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }

    public p2_ArtifactsByKey getP2_artifactsbykey() {
        return p2_artifactsbykey;
    }

    public void setP2_artifactsbykey(p2_ArtifactsByKey p2_artifactsbykey) {
        this.p2_artifactsbykey = p2_artifactsbykey;
    }

}