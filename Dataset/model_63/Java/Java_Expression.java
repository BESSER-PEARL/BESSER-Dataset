





import java.util.List;
import java.util.ArrayList;

public class Java_Expression extends ASTNode {






    private Java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration;




    private Java_AbstractMethodInvocation java_abstractmethodinvocation;




    private Java_EnumConstantDeclaration java_enumconstantdeclaration;


    public Java_Expression(
    ) {
        super(
        );
    }



    public Java_AnnotationTypeMemberDeclaration getJava_annotationtypememberdeclaration() {
        return java_annotationtypememberdeclaration;
    }

    public void setJava_annotationtypememberdeclaration(Java_AnnotationTypeMemberDeclaration java_annotationtypememberdeclaration) {
        this.java_annotationtypememberdeclaration = java_annotationtypememberdeclaration;
    }
    public Java_AbstractMethodInvocation getJava_abstractmethodinvocation() {
        return java_abstractmethodinvocation;
    }

    public void setJava_abstractmethodinvocation(Java_AbstractMethodInvocation java_abstractmethodinvocation) {
        this.java_abstractmethodinvocation = java_abstractmethodinvocation;
    }
    public Java_EnumConstantDeclaration getJava_enumconstantdeclaration() {
        return java_enumconstantdeclaration;
    }

    public void setJava_enumconstantdeclaration(Java_EnumConstantDeclaration java_enumconstantdeclaration) {
        this.java_enumconstantdeclaration = java_enumconstantdeclaration;
    }

}