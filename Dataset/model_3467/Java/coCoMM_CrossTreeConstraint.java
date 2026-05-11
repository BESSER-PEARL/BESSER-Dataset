





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CrossTreeConstraint  {






    private List<coCoMM_CTConstraintExpression> cocomm_ctconstraintexpressions;




    private coCoMM_FeatureModel cocomm_featuremodel;


    public coCoMM_CrossTreeConstraint(
    ) {
        this.cocomm_ctconstraintexpressions = new ArrayList<>();
    }

    public coCoMM_CrossTreeConstraint(
        ArrayList<coCoMM_CTConstraintExpression> cocomm_ctconstraintexpressions    ) {
        this.cocomm_ctconstraintexpressions = cocomm_ctconstraintexpressions;
    }


    public List<coCoMM_CTConstraintExpression> getCocomm_ctconstraintexpressions() {
        return cocomm_ctconstraintexpressions;
    }

    public void addCocomm_ctconstraintexpression(Cocomm_ctconstraintexpression cocomm_ctconstraintexpression) {
        this.cocomm_ctconstraintexpressions.add(cocomm_ctconstraintexpression);
    }
    public coCoMM_FeatureModel getCocomm_featuremodel() {
        return cocomm_featuremodel;
    }

    public void setCocomm_featuremodel(coCoMM_FeatureModel cocomm_featuremodel) {
        this.cocomm_featuremodel = cocomm_featuremodel;
    }

}