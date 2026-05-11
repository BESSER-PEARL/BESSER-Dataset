





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_StatementBlock  {

    private String id;
    private String reference;
    private boolean protected;





    private MOFScriptModel_MOFScriptStatementOwner mofscriptmodel_mofscriptstatementowner;




    private List<MOFScriptModel_MOFScriptStatement> mofscriptmodel_mofscriptstatements;


    public MOFScriptModel_StatementBlock(
        String id,        String reference,        boolean protected    ) {
        this.id = id;
        this.reference = reference;
        this.protected = protected;
        this.mofscriptmodel_mofscriptstatements = new ArrayList<>();
    }

    public MOFScriptModel_StatementBlock(
        String id,        String reference,        boolean protected        ArrayList<MOFScriptModel_MOFScriptStatement> mofscriptmodel_mofscriptstatements    ) {
        this.id = id;
        this.reference = reference;
        this.protected = protected;
        this.mofscriptmodel_mofscriptstatements = mofscriptmodel_mofscriptstatements;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public boolean getProtected() {
        return protected;
    }

    public void setProtected(boolean protected) {
        this.protected = protected;
    }

    public MOFScriptModel_MOFScriptStatementOwner getMofscriptmodel_mofscriptstatementowner() {
        return mofscriptmodel_mofscriptstatementowner;
    }

    public void setMofscriptmodel_mofscriptstatementowner(MOFScriptModel_MOFScriptStatementOwner mofscriptmodel_mofscriptstatementowner) {
        this.mofscriptmodel_mofscriptstatementowner = mofscriptmodel_mofscriptstatementowner;
    }
    public List<MOFScriptModel_MOFScriptStatement> getMofscriptmodel_mofscriptstatements() {
        return mofscriptmodel_mofscriptstatements;
    }

    public void addMofscriptmodel_mofscriptstatement(Mofscriptmodel_mofscriptstatement mofscriptmodel_mofscriptstatement) {
        this.mofscriptmodel_mofscriptstatements.add(mofscriptmodel_mofscriptstatement);
    }

}