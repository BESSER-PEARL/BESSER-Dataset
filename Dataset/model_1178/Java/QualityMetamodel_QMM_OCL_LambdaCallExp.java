





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QMM_OCL_LambdaCallExp extends VariableExp {






    private List<OclExpression> oclexpressions;


    public QualityMetamodel_QMM_OCL_LambdaCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public QualityMetamodel_QMM_OCL_LambdaCallExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}