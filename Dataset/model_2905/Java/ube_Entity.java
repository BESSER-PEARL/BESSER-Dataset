





import java.util.List;
import java.util.ArrayList;

public class ube_Entity extends Type {

    private boolean abstract;





    private List<ube_Feature> ube_features;


    public ube_Entity(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.ube_features = new ArrayList<>();
    }

    public ube_Entity(
        boolean abstract        ArrayList<ube_Feature> ube_features    ) {
        this.abstract = abstract;
        this.ube_features = ube_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<ube_Feature> getUbe_features() {
        return ube_features;
    }

    public void addUbe_feature(Ube_feature ube_feature) {
        this.ube_features.add(ube_feature);
    }

}