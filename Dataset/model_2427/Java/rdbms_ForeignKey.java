





import java.util.List;
import java.util.ArrayList;

public class rdbms_ForeignKey extends Constraints {

    private String updateActionRHS;
    private boolean inverseReferentialIntegrityCon;
    private String deleteActionRHS;
    private String match;



    public rdbms_ForeignKey(
        String updateActionRHS,        boolean inverseReferentialIntegrityCon,        String deleteActionRHS,        String match    ) {
        super(
        );
        this.updateActionRHS = updateActionRHS;
        this.inverseReferentialIntegrityCon = inverseReferentialIntegrityCon;
        this.deleteActionRHS = deleteActionRHS;
        this.match = match;
    }


    public String getUpdateactionrhs() {
        return updateActionRHS;
    }

    public void setUpdateactionrhs(String updateActionRHS) {
        this.updateActionRHS = updateActionRHS;
    }
    public boolean getInversereferentialintegritycon() {
        return inverseReferentialIntegrityCon;
    }

    public void setInversereferentialintegritycon(boolean inverseReferentialIntegrityCon) {
        this.inverseReferentialIntegrityCon = inverseReferentialIntegrityCon;
    }
    public String getDeleteactionrhs() {
        return deleteActionRHS;
    }

    public void setDeleteactionrhs(String deleteActionRHS) {
        this.deleteActionRHS = deleteActionRHS;
    }
    public String getMatch() {
        return match;
    }

    public void setMatch(String match) {
        this.match = match;
    }


}