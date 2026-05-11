





import java.util.List;
import java.util.ArrayList;

public class mitra_ForInit  {






    private mitra_ForStatement mitra_forstatement;




    private List<mitra_StatementExpression> mitra_statementexpressions;




    private List<mitra_LocalVariableDeclaration> mitra_localvariabledeclarations;


    public mitra_ForInit(
    ) {
        this.mitra_statementexpressions = new ArrayList<>();
        this.mitra_localvariabledeclarations = new ArrayList<>();
    }

    public mitra_ForInit(
        ArrayList<mitra_StatementExpression> mitra_statementexpressions,        ArrayList<mitra_LocalVariableDeclaration> mitra_localvariabledeclarations    ) {
        this.mitra_statementexpressions = mitra_statementexpressions;
        this.mitra_localvariabledeclarations = mitra_localvariabledeclarations;
    }


    public mitra_ForStatement getMitra_forstatement() {
        return mitra_forstatement;
    }

    public void setMitra_forstatement(mitra_ForStatement mitra_forstatement) {
        this.mitra_forstatement = mitra_forstatement;
    }
    public List<mitra_StatementExpression> getMitra_statementexpressions() {
        return mitra_statementexpressions;
    }

    public void addMitra_statementexpression(Mitra_statementexpression mitra_statementexpression) {
        this.mitra_statementexpressions.add(mitra_statementexpression);
    }
    public List<mitra_LocalVariableDeclaration> getMitra_localvariabledeclarations() {
        return mitra_localvariabledeclarations;
    }

    public void addMitra_localvariabledeclaration(Mitra_localvariabledeclaration mitra_localvariabledeclaration) {
        this.mitra_localvariabledeclarations.add(mitra_localvariabledeclaration);
    }

}