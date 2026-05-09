





import java.util.List;
import java.util.ArrayList;

public class java_Expression extends ASTNode {






    private java_WhileStatement java_whilestatement;




    private java_AbstractMethodInvocation java_abstractmethodinvocation;




    private java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration;




    private java_EnumConstantDeclaration java_enumconstantdeclaration;


    public java_Expression(
    ) {
        super(
        );
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
    public java_AnnotationTypeMemberDeclaration getJava_annotationtypememberdeclaration() {
        return java_annotationtypememberdeclaration;
    }

    public void setJava_annotationtypememberdeclaration(java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration) {
        this.java_annotationtypememberdeclaration = java_annotationtypememberdeclaration;
    }
    public java_EnumConstantDeclaration getJava_enumconstantdeclaration() {
        return java_enumconstantdeclaration;
    }

    public void setJava_enumconstantdeclaration(java_EnumConstantDeclaration java_enumconstantdeclaration) {
        this.java_enumconstantdeclaration = java_enumconstantdeclaration;
    }

}