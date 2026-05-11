





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IArtifactKey  {

    private String id;
    private String classifier;
    private String version;



    public aggregator_p2_IArtifactKey(
        String id,        String classifier,        String version    ) {
        this.id = id;
        this.classifier = classifier;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}