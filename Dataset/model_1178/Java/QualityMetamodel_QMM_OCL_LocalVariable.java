





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QMM_OCL_LocalVariable extends VariableDeclaration {

    private String eq;





    private OclExpression oclexpression;


    public QualityMetamodel_QMM_OCL_LocalVariable(
        String eq    ) {
        super(
        );
        this.eq = eq;
    }


    public String getEq() {
        return eq;
    }

    public void setEq(String eq) {
        this.eq = eq;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}