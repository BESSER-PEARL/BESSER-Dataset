





import java.util.List;
import java.util.ArrayList;

public class features_modeling_PropositionOR  {






    private features_modeling_PropFormulaCNF features_modeling_propformulacnf;




    private List<features_modeling_Feature> features_modeling_features;


    public features_modeling_PropositionOR(
    ) {
        this.features_modeling_features = new ArrayList<>();
    }

    public features_modeling_PropositionOR(
        ArrayList<features_modeling_Feature> features_modeling_features    ) {
        this.features_modeling_features = features_modeling_features;
    }


    public features_modeling_PropFormulaCNF getFeatures_modeling_propformulacnf() {
        return features_modeling_propformulacnf;
    }

    public void setFeatures_modeling_propformulacnf(features_modeling_PropFormulaCNF features_modeling_propformulacnf) {
        this.features_modeling_propformulacnf = features_modeling_propformulacnf;
    }
    public List<features_modeling_Feature> getFeatures_modeling_features() {
        return features_modeling_features;
    }

    public void addFeatures_modeling_feature(Features_modeling_feature features_modeling_feature) {
        this.features_modeling_features.add(features_modeling_feature);
    }

}