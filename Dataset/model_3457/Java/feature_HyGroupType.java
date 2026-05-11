





import java.util.List;
import java.util.ArrayList;

public class feature_HyGroupType extends HyLinearTemporalElement {

    private String type;





    private feature_HyGroup feature_hygroup;


    public feature_HyGroupType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public feature_HyGroup getFeature_hygroup() {
        return feature_hygroup;
    }

    public void setFeature_hygroup(feature_HyGroup feature_hygroup) {
        this.feature_hygroup = feature_hygroup;
    }

}