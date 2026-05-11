





import java.util.List;
import java.util.ArrayList;

public class mitra_ForUpdate  {






    private List<mitra_StatementExpression> mitra_statementexpressions;




    private mitra_ForStatement mitra_forstatement;


    public mitra_ForUpdate(
    ) {
        this.mitra_statementexpressions = new ArrayList<>();
    }

    public mitra_ForUpdate(
        ArrayList<mitra_StatementExpression> mitra_statementexpressions    ) {
        this.mitra_statementexpressions = mitra_statementexpressions;
    }


    public List<mitra_StatementExpression> getMitra_statementexpressions() {
        return mitra_statementexpressions;
    }

    public void addMitra_statementexpression(Mitra_statementexpression mitra_statementexpression) {
        this.mitra_statementexpressions.add(mitra_statementexpression);
    }
    public mitra_ForStatement getMitra_forstatement() {
        return mitra_forstatement;
    }

    public void setMitra_forstatement(mitra_ForStatement mitra_forstatement) {
        this.mitra_forstatement = mitra_forstatement;
    }

}