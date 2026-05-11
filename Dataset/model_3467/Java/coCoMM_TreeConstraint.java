





import java.util.List;
import java.util.ArrayList;

public class coCoMM_TreeConstraint  {

    private String type;





    private coCoMM_Feature cocomm_feature;




    private List<coCoMM_Feature> cocomm_features;


    public coCoMM_TreeConstraint(
        String type    ) {
        this.type = type;
        this.cocomm_features = new ArrayList<>();
    }

    public coCoMM_TreeConstraint(
        String type        ArrayList<coCoMM_Feature> cocomm_features    ) {
        this.type = type;
        this.cocomm_features = cocomm_features;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public coCoMM_Feature getCocomm_feature() {
        return cocomm_feature;
    }

    public void setCocomm_feature(coCoMM_Feature cocomm_feature) {
        this.cocomm_feature = cocomm_feature;
    }
    public List<coCoMM_Feature> getCocomm_features() {
        return cocomm_features;
    }

    public void addCocomm_feature(Cocomm_feature cocomm_feature) {
        this.cocomm_features.add(cocomm_feature);
    }

}