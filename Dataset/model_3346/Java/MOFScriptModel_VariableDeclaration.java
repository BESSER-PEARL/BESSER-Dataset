





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_VariableDeclaration extends MOFScriptObject {

    private boolean constant;
    private String type;
    private String name;





    private MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation;




    private MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation;




    private MOFScriptModel_MOFScriptStatementOwner mofscriptmodel_mofscriptstatementowner;


    public MOFScriptModel_VariableDeclaration(
        boolean constant,        String type,        String name    ) {
        super(
        );
        this.constant = constant;
        this.type = type;
        this.name = name;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MOFScriptModel_MOFScriptTransformation getMofscriptmodel_mofscripttransformation() {
        return mofscriptmodel_mofscripttransformation;
    }

    public void setMofscriptmodel_mofscripttransformation(MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation) {
        this.mofscriptmodel_mofscripttransformation = mofscriptmodel_mofscripttransformation;
    }
    public MOFScriptModel_MOFScriptTransformation getMofscriptmodel_mofscripttransformation() {
        return mofscriptmodel_mofscripttransformation;
    }

    public void setMofscriptmodel_mofscripttransformation(MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation) {
        this.mofscriptmodel_mofscripttransformation = mofscriptmodel_mofscripttransformation;
    }
    public MOFScriptModel_MOFScriptStatementOwner getMofscriptmodel_mofscriptstatementowner() {
        return mofscriptmodel_mofscriptstatementowner;
    }

    public void setMofscriptmodel_mofscriptstatementowner(MOFScriptModel_MOFScriptStatementOwner mofscriptmodel_mofscriptstatementowner) {
        this.mofscriptmodel_mofscriptstatementowner = mofscriptmodel_mofscriptstatementowner;
    }

}