





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CMConstraintExpression  {

    private String op;





    private List<coCoMM_Feature> cocomm_features;




    private coCoMM_CrossModelConstraint cocomm_crossmodelconstraint;




    private List<coCoMM_CMConstraintExpression> cocomm_cmconstraintexpressions;


    public coCoMM_CMConstraintExpression(
        String op    ) {
        this.op = op;
        this.cocomm_features = new ArrayList<>();
        this.cocomm_cmconstraintexpressions = new ArrayList<>();
    }

    public coCoMM_CMConstraintExpression(
        String op        ArrayList<coCoMM_Feature> cocomm_features,        ArrayList<coCoMM_CMConstraintExpression> cocomm_cmconstraintexpressions    ) {
        this.op = op;
        this.cocomm_features = cocomm_features;
        this.cocomm_cmconstraintexpressions = cocomm_cmconstraintexpressions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<coCoMM_Feature> getCocomm_features() {
        return cocomm_features;
    }

    public void addCocomm_feature(Cocomm_feature cocomm_feature) {
        this.cocomm_features.add(cocomm_feature);
    }
    public coCoMM_CrossModelConstraint getCocomm_crossmodelconstraint() {
        return cocomm_crossmodelconstraint;
    }

    public void setCocomm_crossmodelconstraint(coCoMM_CrossModelConstraint cocomm_crossmodelconstraint) {
        this.cocomm_crossmodelconstraint = cocomm_crossmodelconstraint;
    }
    public List<coCoMM_CMConstraintExpression> getCocomm_cmconstraintexpressions() {
        return cocomm_cmconstraintexpressions;
    }

    public void addCocomm_cmconstraintexpression(Cocomm_cmconstraintexpression cocomm_cmconstraintexpression) {
        this.cocomm_cmconstraintexpressions.add(cocomm_cmconstraintexpression);
    }

}