





import java.util.List;
import java.util.ArrayList;

public class feature_SimpleFeature extends SimpleIdentifier {

    private String valueString;





    private feature_FeatureSet feature_featureset;




    private feature_SimpleOntologyTerm feature_simpleontologyterm;


    public feature_SimpleFeature(
        String valueString    ) {
        super(
        );
        this.valueString = valueString;
    }


    public String getValuestring() {
        return valueString;
    }

    public void setValuestring(String valueString) {
        this.valueString = valueString;
    }

    public feature_FeatureSet getFeature_featureset() {
        return feature_featureset;
    }

    public void setFeature_featureset(feature_FeatureSet feature_featureset) {
        this.feature_featureset = feature_featureset;
    }
    public feature_SimpleOntologyTerm getFeature_simpleontologyterm() {
        return feature_simpleontologyterm;
    }

    public void setFeature_simpleontologyterm(feature_SimpleOntologyTerm feature_simpleontologyterm) {
        this.feature_simpleontologyterm = feature_simpleontologyterm;
    }

}