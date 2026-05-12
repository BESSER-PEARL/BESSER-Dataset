





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IArtifactKey  {

    private String id;
    private String version;
    private String classifier;



    public aggregator_p2_IArtifactKey(
        String id,        String version,        String classifier    ) {
        this.id = id;
        this.version = version;
        this.classifier = classifier;
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
    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }


}