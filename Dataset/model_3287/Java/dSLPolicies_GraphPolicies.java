





import java.util.List;
import java.util.ArrayList;

public class dSLPolicies_GraphPolicies  {

    private String graphModelPolicies;





    private dSLPolicies_Model dslpolicies_model;


    public dSLPolicies_GraphPolicies(
        String graphModelPolicies    ) {
        this.graphModelPolicies = graphModelPolicies;
    }


    public String getGraphmodelpolicies() {
        return graphModelPolicies;
    }

    public void setGraphmodelpolicies(String graphModelPolicies) {
        this.graphModelPolicies = graphModelPolicies;
    }

    public dSLPolicies_Model getDslpolicies_model() {
        return dslpolicies_model;
    }

    public void setDslpolicies_model(dSLPolicies_Model dslpolicies_model) {
        this.dslpolicies_model = dslpolicies_model;
    }

}