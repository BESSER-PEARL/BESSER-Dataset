





import java.util.List;
import java.util.ArrayList;

public class java_Expression extends ASTNode {






    private java_ThrowStatement java_throwstatement;




    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private java_SwitchCase java_switchcase;




    private java_WhileStatement java_whilestatement;


    public java_Expression(
    ) {
        super(
        );
    }



    public java_ThrowStatement getJava_throwstatement() {
        return java_throwstatement;
    }

    public void setJava_throwstatement(java_ThrowStatement java_throwstatement) {
        this.java_throwstatement = java_throwstatement;
    }
    public java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public java_SwitchCase getJava_switchcase() {
        return java_switchcase;
    }

    public void setJava_switchcase(java_SwitchCase java_switchcase) {
        this.java_switchcase = java_switchcase;
    }
    public java_WhileStatement getJava_whilestatement() {
        return java_whilestatement;
    }

    public void setJava_whilestatement(java_WhileStatement java_whilestatement) {
        this.java_whilestatement = java_whilestatement;
    }

}