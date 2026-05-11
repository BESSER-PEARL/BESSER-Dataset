





import java.util.List;
import java.util.ArrayList;

public class alf_OperationCallExpression extends SuffixExpression {

    private String operationName;





    private alf_Tuple alf_tuple;




    private alf_SuffixExpression alf_suffixexpression;


    public alf_OperationCallExpression(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
    }


    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }

    public alf_Tuple getAlf_tuple() {
        return alf_tuple;
    }

    public void setAlf_tuple(alf_Tuple alf_tuple) {
        this.alf_tuple = alf_tuple;
    }
    public alf_SuffixExpression getAlf_suffixexpression() {
        return alf_suffixexpression;
    }

    public void setAlf_suffixexpression(alf_SuffixExpression alf_suffixexpression) {
        this.alf_suffixexpression = alf_suffixexpression;
    }

}