





import java.util.List;
import java.util.ArrayList;

public class Java5_Block extends Statement {






    private Java5_TryStatement java5_trystatement;




    private Java5_SynchronizedStatement java5_synchronizedstatement;




    private List<Java5_Statement> java5_statements;




    private Java5_TryStatement java5_trystatement;




    private Java5_Initializer java5_initializer;




    private Java5_CatchClause java5_catchclause;




    private Java5_MethodDeclaration java5_methoddeclaration;


    public Java5_Block(
    ) {
        super(
        );
        this.java5_statements = new ArrayList<>();
    }

    public Java5_Block(
        ArrayList<Java5_Statement> java5_statements    ) {
        this.java5_statements = java5_statements;
    }


    public Java5_TryStatement getJava5_trystatement() {
        return java5_trystatement;
    }

    public void setJava5_trystatement(Java5_TryStatement java5_trystatement) {
        this.java5_trystatement = java5_trystatement;
    }
    public Java5_SynchronizedStatement getJava5_synchronizedstatement() {
        return java5_synchronizedstatement;
    }

    public void setJava5_synchronizedstatement(Java5_SynchronizedStatement java5_synchronizedstatement) {
        this.java5_synchronizedstatement = java5_synchronizedstatement;
    }
    public List<Java5_Statement> getJava5_statements() {
        return java5_statements;
    }

    public void addJava5_statement(Java5_statement java5_statement) {
        this.java5_statements.add(java5_statement);
    }
    public Java5_TryStatement getJava5_trystatement() {
        return java5_trystatement;
    }

    public void setJava5_trystatement(Java5_TryStatement java5_trystatement) {
        this.java5_trystatement = java5_trystatement;
    }
    public Java5_Initializer getJava5_initializer() {
        return java5_initializer;
    }

    public void setJava5_initializer(Java5_Initializer java5_initializer) {
        this.java5_initializer = java5_initializer;
    }
    public Java5_CatchClause getJava5_catchclause() {
        return java5_catchclause;
    }

    public void setJava5_catchclause(Java5_CatchClause java5_catchclause) {
        this.java5_catchclause = java5_catchclause;
    }
    public Java5_MethodDeclaration getJava5_methoddeclaration() {
        return java5_methoddeclaration;
    }

    public void setJava5_methoddeclaration(Java5_MethodDeclaration java5_methoddeclaration) {
        this.java5_methoddeclaration = java5_methoddeclaration;
    }

}