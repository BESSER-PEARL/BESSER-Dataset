





import java.util.List;
import java.util.ArrayList;

public class fM_Constraints  {






    private List<fM_Rule> fm_rules;




    private fM_FeatureModel fm_featuremodel;


    public fM_Constraints(
    ) {
        this.fm_rules = new ArrayList<>();
    }

    public fM_Constraints(
        ArrayList<fM_Rule> fm_rules    ) {
        this.fm_rules = fm_rules;
    }


    public List<fM_Rule> getFm_rules() {
        return fm_rules;
    }

    public void addFm_rule(Fm_rule fm_rule) {
        this.fm_rules.add(fm_rule);
    }
    public fM_FeatureModel getFm_featuremodel() {
        return fm_featuremodel;
    }

    public void setFm_featuremodel(fM_FeatureModel fm_featuremodel) {
        this.fm_featuremodel = fm_featuremodel;
    }

}