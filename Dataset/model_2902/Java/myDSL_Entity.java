





import java.util.List;
import java.util.ArrayList;

public class myDSL_Entity extends Type {

    private boolean abstract;





    private List<myDSL_Feature> mydsl_features;


    public myDSL_Entity(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.mydsl_features = new ArrayList<>();
    }

    public myDSL_Entity(
        boolean abstract        ArrayList<myDSL_Feature> mydsl_features    ) {
        this.abstract = abstract;
        this.mydsl_features = mydsl_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<myDSL_Feature> getMydsl_features() {
        return mydsl_features;
    }

    public void addMydsl_feature(Mydsl_feature mydsl_feature) {
        this.mydsl_features.add(mydsl_feature);
    }

}