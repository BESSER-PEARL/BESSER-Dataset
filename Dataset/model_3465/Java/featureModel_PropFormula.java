





import java.util.List;
import java.util.ArrayList;

public class featureModel_PropFormula  {






    private List<featureModel_Proposition> featuremodel_propositions;




    private List<featureModel_Proposition> featuremodel_propositions;




    private featureModel_FeatureModel featuremodel_featuremodel;


    public featureModel_PropFormula(
    ) {
        this.featuremodel_propositions = new ArrayList<>();
        this.featuremodel_propositions = new ArrayList<>();
    }

    public featureModel_PropFormula(
        ArrayList<featureModel_Proposition> featuremodel_propositions,        ArrayList<featureModel_Proposition> featuremodel_propositions    ) {
        this.featuremodel_propositions = featuremodel_propositions;
        this.featuremodel_propositions = featuremodel_propositions;
    }


    public List<featureModel_Proposition> getFeaturemodel_propositions() {
        return featuremodel_propositions;
    }

    public void addFeaturemodel_proposition(Featuremodel_proposition featuremodel_proposition) {
        this.featuremodel_propositions.add(featuremodel_proposition);
    }
    public List<featureModel_Proposition> getFeaturemodel_propositions() {
        return featuremodel_propositions;
    }

    public void addFeaturemodel_proposition(Featuremodel_proposition featuremodel_proposition) {
        this.featuremodel_propositions.add(featuremodel_proposition);
    }
    public featureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}