





import java.util.List;
import java.util.ArrayList;

public class model_Comparison extends Condition {

    private String rhs;
    private String lhs;





    private model_ComparisonOperator model_comparisonoperator;


    public model_Comparison(
        String rhs,        String lhs    ) {
        super(
        );
        this.rhs = rhs;
        this.lhs = lhs;
    }


    public String getRhs() {
        return rhs;
    }

    public void setRhs(String rhs) {
        this.rhs = rhs;
    }
    public String getLhs() {
        return lhs;
    }

    public void setLhs(String lhs) {
        this.lhs = lhs;
    }

    public model_ComparisonOperator getModel_comparisonoperator() {
        return model_comparisonoperator;
    }

    public void setModel_comparisonoperator(model_ComparisonOperator model_comparisonoperator) {
        this.model_comparisonoperator = model_comparisonoperator;
    }

}