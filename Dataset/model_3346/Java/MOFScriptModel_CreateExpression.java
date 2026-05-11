





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_CreateExpression extends Expression {

    private String type;





    private List<MOFScriptModel_CreateExpressionParameter> mofscriptmodel_createexpressionparameters;


    public MOFScriptModel_CreateExpression(
        String type    ) {
        super(
        );
        this.type = type;
        this.mofscriptmodel_createexpressionparameters = new ArrayList<>();
    }

    public MOFScriptModel_CreateExpression(
        String type        ArrayList<MOFScriptModel_CreateExpressionParameter> mofscriptmodel_createexpressionparameters    ) {
        this.type = type;
        this.mofscriptmodel_createexpressionparameters = mofscriptmodel_createexpressionparameters;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<MOFScriptModel_CreateExpressionParameter> getMofscriptmodel_createexpressionparameters() {
        return mofscriptmodel_createexpressionparameters;
    }

    public void addMofscriptmodel_createexpressionparameter(Mofscriptmodel_createexpressionparameter mofscriptmodel_createexpressionparameter) {
        this.mofscriptmodel_createexpressionparameters.add(mofscriptmodel_createexpressionparameter);
    }

}