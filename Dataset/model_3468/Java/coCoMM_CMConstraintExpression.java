





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CMConstraintExpression  {

    private String op;





    private List<coCoMM_CMConstraintExpression> cocomm_cmconstraintexpressions;




    private List<coCoMM_Feature> cocomm_features;




    private coCoMM_CrossModelConstraint cocomm_crossmodelconstraint;


    public coCoMM_CMConstraintExpression(
        String op    ) {
        this.op = op;
        this.cocomm_cmconstraintexpressions = new ArrayList<>();
        this.cocomm_features = new ArrayList<>();
    }

    public coCoMM_CMConstraintExpression(
        String op        ArrayList<coCoMM_CMConstraintExpression> cocomm_cmconstraintexpressions,        ArrayList<coCoMM_Feature> cocomm_features    ) {
        this.op = op;
        this.cocomm_cmconstraintexpressions = cocomm_cmconstraintexpressions;
        this.cocomm_features = cocomm_features;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<coCoMM_CMConstraintExpression> getCocomm_cmconstraintexpressions() {
        return cocomm_cmconstraintexpressions;
    }

    public void addCocomm_cmconstraintexpression(Cocomm_cmconstraintexpression cocomm_cmconstraintexpression) {
        this.cocomm_cmconstraintexpressions.add(cocomm_cmconstraintexpression);
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

}