





import java.util.List;
import java.util.ArrayList;

public class javaMM_Block extends Statement {






    private javaMM_Initializer javamm_initializer;




    private List<javaMM_Statement> javamm_statements;




    private javaMM_SynchronizedStatement javamm_synchronizedstatement;




    private javaMM_TryStatement javamm_trystatement;




    private javaMM_TryStatement javamm_trystatement;




    private javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration;


    public javaMM_Block(
    ) {
        super(
        );
        this.javamm_statements = new ArrayList<>();
    }

    public javaMM_Block(
        ArrayList<javaMM_Statement> javamm_statements    ) {
        this.javamm_statements = javamm_statements;
    }


    public javaMM_Initializer getJavamm_initializer() {
        return javamm_initializer;
    }

    public void setJavamm_initializer(javaMM_Initializer javamm_initializer) {
        this.javamm_initializer = javamm_initializer;
    }
    public List<javaMM_Statement> getJavamm_statements() {
        return javamm_statements;
    }

    public void addJavamm_statement(Javamm_statement javamm_statement) {
        this.javamm_statements.add(javamm_statement);
    }
    public javaMM_SynchronizedStatement getJavamm_synchronizedstatement() {
        return javamm_synchronizedstatement;
    }

    public void setJavamm_synchronizedstatement(javaMM_SynchronizedStatement javamm_synchronizedstatement) {
        this.javamm_synchronizedstatement = javamm_synchronizedstatement;
    }
    public javaMM_TryStatement getJavamm_trystatement() {
        return javamm_trystatement;
    }

    public void setJavamm_trystatement(javaMM_TryStatement javamm_trystatement) {
        this.javamm_trystatement = javamm_trystatement;
    }
    public javaMM_TryStatement getJavamm_trystatement() {
        return javamm_trystatement;
    }

    public void setJavamm_trystatement(javaMM_TryStatement javamm_trystatement) {
        this.javamm_trystatement = javamm_trystatement;
    }
    public javaMM_AbstractMethodDeclaration getJavamm_abstractmethoddeclaration() {
        return javamm_abstractmethoddeclaration;
    }

    public void setJavamm_abstractmethoddeclaration(javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration) {
        this.javamm_abstractmethoddeclaration = javamm_abstractmethoddeclaration;
    }

}