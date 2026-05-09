





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBFetchCursorStatement extends RDBCursorStatement {






    private List<RDBHostVariableReference> rdbhostvariablereferences;


    public astm_sastm_RDBFetchCursorStatement(
    ) {
        super(
        );
        this.rdbhostvariablereferences = new ArrayList<>();
    }

    public astm_sastm_RDBFetchCursorStatement(
        ArrayList<RDBHostVariableReference> rdbhostvariablereferences    ) {
        this.rdbhostvariablereferences = rdbhostvariablereferences;
    }


    public List<RDBHostVariableReference> getRdbhostvariablereferences() {
        return rdbhostvariablereferences;
    }

    public void addRdbhostvariablereference(Rdbhostvariablereference rdbhostvariablereference) {
        this.rdbhostvariablereferences.add(rdbhostvariablereference);
    }

}