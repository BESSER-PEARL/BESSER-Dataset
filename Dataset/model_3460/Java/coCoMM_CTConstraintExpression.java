





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CTConstraintExpression  {

    private String op;





    private coCoMM_CrossTreeConstraint cocomm_crosstreeconstraint;




    private List<coCoMM_CTConstraintExpression> cocomm_ctconstraintexpressions;




    private List<coCoMM_Feature> cocomm_features;


    public coCoMM_CTConstraintExpression(
        String op    ) {
        this.op = op;
        this.cocomm_ctconstraintexpressions = new ArrayList<>();
        this.cocomm_features = new ArrayList<>();
    }

    public coCoMM_CTConstraintExpression(
        String op        ArrayList<coCoMM_CTConstraintExpression> cocomm_ctconstraintexpressions,        ArrayList<coCoMM_Feature> cocomm_features    ) {
        this.op = op;
        this.cocomm_ctconstraintexpressions = cocomm_ctconstraintexpressions;
        this.cocomm_features = cocomm_features;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public coCoMM_CrossTreeConstraint getCocomm_crosstreeconstraint() {
        return cocomm_crosstreeconstraint;
    }

    public void setCocomm_crosstreeconstraint(coCoMM_CrossTreeConstraint cocomm_crosstreeconstraint) {
        this.cocomm_crosstreeconstraint = cocomm_crosstreeconstraint;
    }
    public List<coCoMM_CTConstraintExpression> getCocomm_ctconstraintexpressions() {
        return cocomm_ctconstraintexpressions;
    }

    public void addCocomm_ctconstraintexpression(Cocomm_ctconstraintexpression cocomm_ctconstraintexpression) {
        this.cocomm_ctconstraintexpressions.add(cocomm_ctconstraintexpression);
    }
    public List<coCoMM_Feature> getCocomm_features() {
        return cocomm_features;
    }

    public void addCocomm_feature(Cocomm_feature cocomm_feature) {
        this.cocomm_features.add(cocomm_feature);
    }

}