





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_FileStatement extends MOFScriptStatement {

    private boolean use;
    private String fileReference;
    private boolean append;





    private MOFScriptModel_ValueExpression mofscriptmodel_valueexpression;


    public MOFScriptModel_FileStatement(
        boolean use,        String fileReference,        boolean append    ) {
        super(
        );
        this.use = use;
        this.fileReference = fileReference;
        this.append = append;
    }


    public boolean getUse() {
        return use;
    }

    public void setUse(boolean use) {
        this.use = use;
    }
    public String getFilereference() {
        return fileReference;
    }

    public void setFilereference(String fileReference) {
        this.fileReference = fileReference;
    }
    public boolean getAppend() {
        return append;
    }

    public void setAppend(boolean append) {
        this.append = append;
    }

    public MOFScriptModel_ValueExpression getMofscriptmodel_valueexpression() {
        return mofscriptmodel_valueexpression;
    }

    public void setMofscriptmodel_valueexpression(MOFScriptModel_ValueExpression mofscriptmodel_valueexpression) {
        this.mofscriptmodel_valueexpression = mofscriptmodel_valueexpression;
    }

}