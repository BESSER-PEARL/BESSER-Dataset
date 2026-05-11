





import java.util.List;
import java.util.ArrayList;

public class ER_EntityType extends NamedElement {






    private ER_Reference er_reference;




    private ER_ERModel er_ermodel;




    private List<ER_Feature> er_features;


    public ER_EntityType(
    ) {
        super(
        );
        this.er_features = new ArrayList<>();
    }

    public ER_EntityType(
        ArrayList<ER_Feature> er_features    ) {
        this.er_features = er_features;
    }


    public ER_Reference getEr_reference() {
        return er_reference;
    }

    public void setEr_reference(ER_Reference er_reference) {
        this.er_reference = er_reference;
    }
    public ER_ERModel getEr_ermodel() {
        return er_ermodel;
    }

    public void setEr_ermodel(ER_ERModel er_ermodel) {
        this.er_ermodel = er_ermodel;
    }
    public List<ER_Feature> getEr_features() {
        return er_features;
    }

    public void addEr_feature(Er_feature er_feature) {
        this.er_features.add(er_feature);
    }

}