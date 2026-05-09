





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_EOperationCallExp extends EFeatureCallExp {

    private String referredOperation;





    private List<EOclExpression> eoclexpressions;


    public ocl_exp_EOperationCallExp(
        String referredOperation    ) {
        super(
        );
        this.referredOperation = referredOperation;
        this.eoclexpressions = new ArrayList<>();
    }

    public ocl_exp_EOperationCallExp(
        String referredOperation        ArrayList<EOclExpression> eoclexpressions    ) {
        this.referredOperation = referredOperation;
        this.eoclexpressions = eoclexpressions;
    }

    public String getReferredoperation() {
        return referredOperation;
    }

    public void setReferredoperation(String referredOperation) {
        this.referredOperation = referredOperation;
    }

    public List<EOclExpression> getEoclexpressions() {
        return eoclexpressions;
    }

    public void addEoclexpression(Eoclexpression eoclexpression) {
        this.eoclexpressions.add(eoclexpression);
    }

}