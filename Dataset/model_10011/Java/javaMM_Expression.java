





import java.util.List;
import java.util.ArrayList;

public class javaMM_Expression extends ASTNode {






    private javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation;




    private javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration;




    private javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration;


    public javaMM_Expression(
    ) {
        super(
        );
    }



    public javaMM_AbstractMethodInvocation getJavamm_abstractmethodinvocation() {
        return javamm_abstractmethodinvocation;
    }

    public void setJavamm_abstractmethodinvocation(javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation) {
        this.javamm_abstractmethodinvocation = javamm_abstractmethodinvocation;
    }
    public javaMM_EnumConstantDeclaration getJavamm_enumconstantdeclaration() {
        return javamm_enumconstantdeclaration;
    }

    public void setJavamm_enumconstantdeclaration(javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration) {
        this.javamm_enumconstantdeclaration = javamm_enumconstantdeclaration;
    }
    public javaMM_AnnotationTypeMemberDeclaration getJavamm_annotationtypememberdeclaration() {
        return javamm_annotationtypememberdeclaration;
    }

    public void setJavamm_annotationtypememberdeclaration(javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration) {
        this.javamm_annotationtypememberdeclaration = javamm_annotationtypememberdeclaration;
    }

}