





import java.util.List;
import java.util.ArrayList;

public class fm_FeatureModel  {

    private String version;
    private String comment;
    private String description;
    private String name;





    private fm_Feature fm_feature;




    private fm_Feature fm_feature;




    private List<fm_Feature> fm_features;


    public fm_FeatureModel(
        String version,        String comment,        String description,        String name    ) {
        this.version = version;
        this.comment = comment;
        this.description = description;
        this.name = name;
        this.fm_features = new ArrayList<>();
    }

    public fm_FeatureModel(
        String version,        String comment,        String description,        String name        ArrayList<fm_Feature> fm_features    ) {
        this.version = version;
        this.comment = comment;
        this.description = description;
        this.name = name;
        this.fm_features = fm_features;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public List<fm_Feature> getFm_features() {
        return fm_features;
    }

    public void addFm_feature(Fm_feature fm_feature) {
        this.fm_features.add(fm_feature);
    }

}