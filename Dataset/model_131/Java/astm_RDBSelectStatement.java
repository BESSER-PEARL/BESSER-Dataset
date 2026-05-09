





import java.util.List;
import java.util.ArrayList;

public class astm_RDBSelectStatement extends Statement {






    private List<astm_RDBHostVariableReference> astm_rdbhostvariablereferences;


    public astm_RDBSelectStatement(
    ) {
        super(
        );
        this.astm_rdbhostvariablereferences = new ArrayList<>();
    }

    public astm_RDBSelectStatement(
        ArrayList<astm_RDBHostVariableReference> astm_rdbhostvariablereferences    ) {
        this.astm_rdbhostvariablereferences = astm_rdbhostvariablereferences;
    }


    public List<astm_RDBHostVariableReference> getAstm_rdbhostvariablereferences() {
        return astm_rdbhostvariablereferences;
    }

    public void addAstm_rdbhostvariablereference(Astm_rdbhostvariablereference astm_rdbhostvariablereference) {
        this.astm_rdbhostvariablereferences.add(astm_rdbhostvariablereference);
    }

}