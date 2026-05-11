





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_FunctionCall extends SimpleExpression {

    private boolean isSuperCall;
    private String transformationContext;
    private String name;





    private MOFScriptModel_TransformationRule mofscriptmodel_transformationrule;




    private MOFScriptModel_FunctionCallStatement mofscriptmodel_functioncallstatement;




    private MOFScriptModel_SelectExpression mofscriptmodel_selectexpression;




    private List<MOFScriptModel_ValueExpression> mofscriptmodel_valueexpressions;


    public MOFScriptModel_FunctionCall(
        boolean isSuperCall,        String transformationContext,        String name    ) {
        super(
        );
        this.isSuperCall = isSuperCall;
        this.transformationContext = transformationContext;
        this.name = name;
        this.mofscriptmodel_valueexpressions = new ArrayList<>();
    }

    public MOFScriptModel_FunctionCall(
        boolean isSuperCall,        String transformationContext,        String name        ArrayList<MOFScriptModel_ValueExpression> mofscriptmodel_valueexpressions    ) {
        this.isSuperCall = isSuperCall;
        this.transformationContext = transformationContext;
        this.name = name;
        this.mofscriptmodel_valueexpressions = mofscriptmodel_valueexpressions;
    }

    public boolean getIssupercall() {
        return isSuperCall;
    }

    public void setIssupercall(boolean isSuperCall) {
        this.isSuperCall = isSuperCall;
    }
    public String getTransformationcontext() {
        return transformationContext;
    }

    public void setTransformationcontext(String transformationContext) {
        this.transformationContext = transformationContext;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MOFScriptModel_TransformationRule getMofscriptmodel_transformationrule() {
        return mofscriptmodel_transformationrule;
    }

    public void setMofscriptmodel_transformationrule(MOFScriptModel_TransformationRule mofscriptmodel_transformationrule) {
        this.mofscriptmodel_transformationrule = mofscriptmodel_transformationrule;
    }
    public MOFScriptModel_FunctionCallStatement getMofscriptmodel_functioncallstatement() {
        return mofscriptmodel_functioncallstatement;
    }

    public void setMofscriptmodel_functioncallstatement(MOFScriptModel_FunctionCallStatement mofscriptmodel_functioncallstatement) {
        this.mofscriptmodel_functioncallstatement = mofscriptmodel_functioncallstatement;
    }
    public MOFScriptModel_SelectExpression getMofscriptmodel_selectexpression() {
        return mofscriptmodel_selectexpression;
    }

    public void setMofscriptmodel_selectexpression(MOFScriptModel_SelectExpression mofscriptmodel_selectexpression) {
        this.mofscriptmodel_selectexpression = mofscriptmodel_selectexpression;
    }
    public List<MOFScriptModel_ValueExpression> getMofscriptmodel_valueexpressions() {
        return mofscriptmodel_valueexpressions;
    }

    public void addMofscriptmodel_valueexpression(Mofscriptmodel_valueexpression mofscriptmodel_valueexpression) {
        this.mofscriptmodel_valueexpressions.add(mofscriptmodel_valueexpression);
    }

}