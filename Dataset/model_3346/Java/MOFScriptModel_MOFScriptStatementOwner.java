





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptStatementOwner extends MOFScriptObject {






    private List<MOFScriptModel_MOFScriptStatement> mofscriptmodel_mofscriptstatements;




    private MOFScriptModel_MOFScriptStatement mofscriptmodel_mofscriptstatement;


    public MOFScriptModel_MOFScriptStatementOwner(
    ) {
        super(
        );
        this.mofscriptmodel_mofscriptstatements = new ArrayList<>();
    }

    public MOFScriptModel_MOFScriptStatementOwner(
        ArrayList<MOFScriptModel_MOFScriptStatement> mofscriptmodel_mofscriptstatements    ) {
        this.mofscriptmodel_mofscriptstatements = mofscriptmodel_mofscriptstatements;
    }


    public List<MOFScriptModel_MOFScriptStatement> getMofscriptmodel_mofscriptstatements() {
        return mofscriptmodel_mofscriptstatements;
    }

    public void addMofscriptmodel_mofscriptstatement(Mofscriptmodel_mofscriptstatement mofscriptmodel_mofscriptstatement) {
        this.mofscriptmodel_mofscriptstatements.add(mofscriptmodel_mofscriptstatement);
    }
    public MOFScriptModel_MOFScriptStatement getMofscriptmodel_mofscriptstatement() {
        return mofscriptmodel_mofscriptstatement;
    }

    public void setMofscriptmodel_mofscriptstatement(MOFScriptModel_MOFScriptStatement mofscriptmodel_mofscriptstatement) {
        this.mofscriptmodel_mofscriptstatement = mofscriptmodel_mofscriptstatement;
    }

}