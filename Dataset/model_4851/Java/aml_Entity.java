





import java.util.List;
import java.util.ArrayList;

public class aml_Entity extends AbstractElements {






    private List<aml_Feature> aml_features;


    public aml_Entity(
    ) {
        super(
        );
        this.aml_features = new ArrayList<>();
    }

    public aml_Entity(
        ArrayList<aml_Feature> aml_features    ) {
        this.aml_features = aml_features;
    }


    public List<aml_Feature> getAml_features() {
        return aml_features;
    }

    public void addAml_feature(Aml_feature aml_feature) {
        this.aml_features.add(aml_feature);
    }

}