





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CMConstraintExpression  {

    private String op;





    private List<coCoMM_Feature> cocomm_features;




    private coCoMM_CMConstraintExpression cocomm_cmconstraintexpression;


    public coCoMM_CMConstraintExpression(
        String op    ) {
        this.op = op;
        this.cocomm_features = new ArrayList<>();
    }

    public coCoMM_CMConstraintExpression(
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

    public List<coCoMM_Feature> getCocomm_features() {
        return cocomm_features;
    }

    public void addCocomm_feature(Cocomm_feature cocomm_feature) {
        this.cocomm_features.add(cocomm_feature);
    }
    public coCoMM_CMConstraintExpression getCocomm_cmconstraintexpression() {
        return cocomm_cmconstraintexpression;
    }

    public void setCocomm_cmconstraintexpression(coCoMM_CMConstraintExpression cocomm_cmconstraintexpression) {
        this.cocomm_cmconstraintexpression = cocomm_cmconstraintexpression;
    }

}