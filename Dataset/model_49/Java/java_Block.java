





import java.util.List;
import java.util.ArrayList;

public class java_Block extends Statement {






    private List<java_Statement> java_statements;




    private java_TryStatement java_trystatement;




    private java_TryStatement java_trystatement;




    private java_AbstractMethodDeclaration java_abstractmethoddeclaration;




    private java_SynchronizedStatement java_synchronizedstatement;




    private java_Initializer java_initializer;


    public java_Block(
    ) {
        super(
        );
        this.java_statements = new ArrayList<>();
    }

    public java_Block(
        ArrayList<java_Statement> java_statements    ) {
        this.java_statements = java_statements;
    }


    public List<java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }
    public java_TryStatement getJava_trystatement() {
        return java_trystatement;
    }

    public void setJava_trystatement(java_TryStatement java_trystatement) {
        this.java_trystatement = java_trystatement;
    }
    public java_TryStatement getJava_trystatement() {
        return java_trystatement;
    }

    public void setJava_trystatement(java_TryStatement java_trystatement) {
        this.java_trystatement = java_trystatement;
    }
    public java_AbstractMethodDeclaration getJava_abstractmethoddeclaration() {
        return java_abstractmethoddeclaration;
    }

    public void setJava_abstractmethoddeclaration(java_AbstractMethodDeclaration java_abstractmethoddeclaration) {
        this.java_abstractmethoddeclaration = java_abstractmethoddeclaration;
    }
    public java_SynchronizedStatement getJava_synchronizedstatement() {
        return java_synchronizedstatement;
    }

    public void setJava_synchronizedstatement(java_SynchronizedStatement java_synchronizedstatement) {
        this.java_synchronizedstatement = java_synchronizedstatement;
    }
    public java_Initializer getJava_initializer() {
        return java_initializer;
    }

    public void setJava_initializer(java_Initializer java_initializer) {
        this.java_initializer = java_initializer;
    }

}