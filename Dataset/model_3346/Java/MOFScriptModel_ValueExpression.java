





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_ValueExpression extends Expression {

    private String specification;





    private MOFScriptModel_CreateExpressionParameter mofscriptmodel_createexpressionparameter;


    public MOFScriptModel_ValueExpression(
        String specification    ) {
        super(
        );
        this.specification = specification;
    }


    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public MOFScriptModel_CreateExpressionParameter getMofscriptmodel_createexpressionparameter() {
        return mofscriptmodel_createexpressionparameter;
    }

    public void setMofscriptmodel_createexpressionparameter(MOFScriptModel_CreateExpressionParameter mofscriptmodel_createexpressionparameter) {
        this.mofscriptmodel_createexpressionparameter = mofscriptmodel_createexpressionparameter;
    }

}