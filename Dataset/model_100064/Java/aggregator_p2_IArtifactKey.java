





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IArtifactKey  {

    private String classifier;
    private String version;
    private String id;



    public aggregator_p2_IArtifactKey(
        String classifier,        String version,        String id    ) {
        this.classifier = classifier;
        this.version = version;
        this.id = id;
    }


    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
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


}