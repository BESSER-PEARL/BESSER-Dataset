





import java.util.List;
import java.util.ArrayList;

public class featuremodel_FeatureModel  {

    private String version;
    private String id;



    public featuremodel_FeatureModel(
        String version,        String id    ) {
        this.version = version;
        this.id = id;
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