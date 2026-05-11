





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_PrintStatement extends MOFScriptStatement {

    private String printCommand;
    private String context;





    private MOFScriptModel_ValueExpression mofscriptmodel_valueexpression;


    public MOFScriptModel_PrintStatement(
        String printCommand,        String context    ) {
        super(
        );
        this.printCommand = printCommand;
        this.context = context;
    }


    public String getPrintcommand() {
        return printCommand;
    }

    public void setPrintcommand(String printCommand) {
        this.printCommand = printCommand;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public MOFScriptModel_ValueExpression getMofscriptmodel_valueexpression() {
        return mofscriptmodel_valueexpression;
    }

    public void setMofscriptmodel_valueexpression(MOFScriptModel_ValueExpression mofscriptmodel_valueexpression) {
        this.mofscriptmodel_valueexpression = mofscriptmodel_valueexpression;
    }

}