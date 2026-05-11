





import java.util.List;
import java.util.ArrayList;

public class hbmxml_Entity extends Type {

    private boolean abstract;





    private List<hbmxml_Feature> hbmxml_features;


    public hbmxml_Entity(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.hbmxml_features = new ArrayList<>();
    }

    public hbmxml_Entity(
        boolean abstract        ArrayList<hbmxml_Feature> hbmxml_features    ) {
        this.abstract = abstract;
        this.hbmxml_features = hbmxml_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<hbmxml_Feature> getHbmxml_features() {
        return hbmxml_features;
    }

    public void addHbmxml_feature(Hbmxml_feature hbmxml_feature) {
        this.hbmxml_features.add(hbmxml_feature);
    }

}