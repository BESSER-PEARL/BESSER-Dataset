





import java.util.List;
import java.util.ArrayList;

public class forms_Entity extends Type {

    private boolean abstract;





    private List<forms_Feature> forms_features;


    public forms_Entity(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.forms_features = new ArrayList<>();
    }

    public forms_Entity(
        boolean abstract        ArrayList<forms_Feature> forms_features    ) {
        this.abstract = abstract;
        this.forms_features = forms_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<forms_Feature> getForms_features() {
        return forms_features;
    }

    public void addForms_feature(Forms_feature forms_feature) {
        this.forms_features.add(forms_feature);
    }

}