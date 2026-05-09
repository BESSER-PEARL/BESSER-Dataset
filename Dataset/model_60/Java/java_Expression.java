





import java.util.List;
import java.util.ArrayList;

public class java_Expression extends ASTNode {






    private java_SuperConstructorInvocation java_superconstructorinvocation;




    private java_SynchronizedStatement java_synchronizedstatement;




    private java_WhileStatement java_whilestatement;




    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private java_ThrowStatement java_throwstatement;




    private java_SwitchStatement java_switchstatement;




    private java_SwitchCase java_switchcase;


    public java_Expression(
    ) {
        super(
        );
    }



    public java_SuperConstructorInvocation getJava_superconstructorinvocation() {
        return java_superconstructorinvocation;
    }

    public void setJava_superconstructorinvocation(java_SuperConstructorInvocation java_superconstructorinvocation) {
        this.java_superconstructorinvocation = java_superconstructorinvocation;
    }
    public java_SynchronizedStatement getJava_synchronizedstatement() {
        return java_synchronizedstatement;
    }

    public void setJava_synchronizedstatement(java_SynchronizedStatement java_synchronizedstatement) {
        this.java_synchronizedstatement = java_synchronizedstatement;
    }
    public java_WhileStatement getJava_whilestatement() {
        return java_whilestatement;
    }

    public void setJava_whilestatement(java_WhileStatement java_whilestatement) {
        this.java_whilestatement = java_whilestatement;
    }
    public java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public java_ThrowStatement getJava_throwstatement() {
        return java_throwstatement;
    }

    public void setJava_throwstatement(java_ThrowStatement java_throwstatement) {
        this.java_throwstatement = java_throwstatement;
    }
    public java_SwitchStatement getJava_switchstatement() {
        return java_switchstatement;
    }

    public void setJava_switchstatement(java_SwitchStatement java_switchstatement) {
        this.java_switchstatement = java_switchstatement;
    }
    public java_SwitchCase getJava_switchcase() {
        return java_switchcase;
    }

    public void setJava_switchcase(java_SwitchCase java_switchcase) {
        this.java_switchcase = java_switchcase;
    }

}