





import java.util.List;
import java.util.ArrayList;

public class rdbms_ForeignKey extends Constraints {

    private boolean inverseReferentialIntegrityCon;
    private String updateActionRHS;
    private String match;
    private String deleteActionRHS;





    private rdbms_Table rdbms_table;




    private rdbms_Table rdbms_table;




    private rdbms_Table rdbms_table;




    private rdbms_Column rdbms_column;




    private List<rdbms_Column> rdbms_columns;


    public rdbms_ForeignKey(
        boolean inverseReferentialIntegrityCon,        String updateActionRHS,        String match,        String deleteActionRHS    ) {
        super(
        );
        this.inverseReferentialIntegrityCon = inverseReferentialIntegrityCon;
        this.updateActionRHS = updateActionRHS;
        this.match = match;
        this.deleteActionRHS = deleteActionRHS;
        this.rdbms_columns = new ArrayList<>();
    }

    public rdbms_ForeignKey(
        boolean inverseReferentialIntegrityCon,        String updateActionRHS,        String match,        String deleteActionRHS        ArrayList<rdbms_Column> rdbms_columns    ) {
        this.inverseReferentialIntegrityCon = inverseReferentialIntegrityCon;
        this.updateActionRHS = updateActionRHS;
        this.match = match;
        this.deleteActionRHS = deleteActionRHS;
        this.rdbms_columns = rdbms_columns;
    }

    public boolean getInversereferentialintegritycon() {
        return inverseReferentialIntegrityCon;
    }

    public void setInversereferentialintegritycon(boolean inverseReferentialIntegrityCon) {
        this.inverseReferentialIntegrityCon = inverseReferentialIntegrityCon;
    }
    public String getUpdateactionrhs() {
        return updateActionRHS;
    }

    public void setUpdateactionrhs(String updateActionRHS) {
        this.updateActionRHS = updateActionRHS;
    }
    public String getMatch() {
        return match;
    }

    public void setMatch(String match) {
        this.match = match;
    }
    public String getDeleteactionrhs() {
        return deleteActionRHS;
    }

    public void setDeleteactionrhs(String deleteActionRHS) {
        this.deleteActionRHS = deleteActionRHS;
    }

    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public rdbms_Column getRdbms_column() {
        return rdbms_column;
    }

    public void setRdbms_column(rdbms_Column rdbms_column) {
        this.rdbms_column = rdbms_column;
    }
    public List<rdbms_Column> getRdbms_columns() {
        return rdbms_columns;
    }

    public void addRdbms_column(Rdbms_column rdbms_column) {
        this.rdbms_columns.add(rdbms_column);
    }

}