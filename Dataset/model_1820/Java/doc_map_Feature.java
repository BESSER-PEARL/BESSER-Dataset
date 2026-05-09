





import java.util.List;
import java.util.ArrayList;

public class doc_map_Feature extends Import {

    private boolean createSection;
    private String featureId;



    public doc_map_Feature(
        boolean createSection,        String featureId    ) {
        super(
        );
        this.createSection = createSection;
        this.featureId = featureId;
    }


    public boolean getCreatesection() {
        return createSection;
    }

    public void setCreatesection(boolean createSection) {
        this.createSection = createSection;
    }
    public String getFeatureid() {
        return featureId;
    }

    public void setFeatureid(String featureId) {
        this.featureId = featureId;
    }


}