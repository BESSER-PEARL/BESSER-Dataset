





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CTConstraintExpression  {

    private String op;





    private coCoMM_CTConstraintExpression cocomm_ctconstraintexpression;




    private List<coCoMM_Feature> cocomm_features;




    private coCoMM_CrossTreeConstraint cocomm_crosstreeconstraint;


    public coCoMM_CTConstraintExpression(
        String op    ) {
        this.op = op;
        this.cocomm_features = new ArrayList<>();
    }

    public coCoMM_CTConstraintExpression(
        String op        ArrayList<coCoMM_Feature> cocomm_features    ) {
        this.op = op;
        this.cocomm_features = cocomm_features;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public coCoMM_CTConstraintExpression getCocomm_ctconstraintexpression() {
        return cocomm_ctconstraintexpression;
    }

    public void setCocomm_ctconstraintexpression(coCoMM_CTConstraintExpression cocomm_ctconstraintexpression) {
        this.cocomm_ctconstraintexpression = cocomm_ctconstraintexpression;
    }
    public List<coCoMM_Feature> getCocomm_features() {
        return cocomm_features;
    }

    public void addCocomm_feature(Cocomm_feature cocomm_feature) {
        this.cocomm_features.add(cocomm_feature);
    }
    public coCoMM_CrossTreeConstraint getCocomm_crosstreeconstraint() {
        return cocomm_crosstreeconstraint;
    }

    public void setCocomm_crosstreeconstraint(coCoMM_CrossTreeConstraint cocomm_crosstreeconstraint) {
        this.cocomm_crosstreeconstraint = cocomm_crosstreeconstraint;
    }

}