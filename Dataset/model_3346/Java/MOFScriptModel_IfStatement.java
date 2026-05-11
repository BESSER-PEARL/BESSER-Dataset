





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_IfStatement extends MOFScriptStatement {






    private MOFScriptModel_IfStatement mofscriptmodel_ifstatement;




    private MOFScriptModel_Expression mofscriptmodel_expression;


    public MOFScriptModel_IfStatement(
    ) {
        super(
        );
    }



    public MOFScriptModel_IfStatement getMofscriptmodel_ifstatement() {
        return mofscriptmodel_ifstatement;
    }

    public void setMofscriptmodel_ifstatement(MOFScriptModel_IfStatement mofscriptmodel_ifstatement) {
        this.mofscriptmodel_ifstatement = mofscriptmodel_ifstatement;
    }
    public MOFScriptModel_Expression getMofscriptmodel_expression() {
        return mofscriptmodel_expression;
    }

    public void setMofscriptmodel_expression(MOFScriptModel_Expression mofscriptmodel_expression) {
        this.mofscriptmodel_expression = mofscriptmodel_expression;
    }

}