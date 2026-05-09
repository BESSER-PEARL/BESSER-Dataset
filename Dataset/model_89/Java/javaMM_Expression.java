





import java.util.List;
import java.util.ArrayList;

public class javaMM_Expression extends ASTNode {






    private javaMM_PostfixExpression javamm_postfixexpression;




    private javaMM_PrefixExpression javamm_prefixexpression;




    private javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration;




    private javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation;




    private javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration;


    public javaMM_Expression(
    ) {
        super(
        );
    }



    public javaMM_PostfixExpression getJavamm_postfixexpression() {
        return javamm_postfixexpression;
    }

    public void setJavamm_postfixexpression(javaMM_PostfixExpression javamm_postfixexpression) {
        this.javamm_postfixexpression = javamm_postfixexpression;
    }
    public javaMM_PrefixExpression getJavamm_prefixexpression() {
        return javamm_prefixexpression;
    }

    public void setJavamm_prefixexpression(javaMM_PrefixExpression javamm_prefixexpression) {
        this.javamm_prefixexpression = javamm_prefixexpression;
    }
    public javaMM_EnumConstantDeclaration getJavamm_enumconstantdeclaration() {
        return javamm_enumconstantdeclaration;
    }

    public void setJavamm_enumconstantdeclaration(javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration) {
        this.javamm_enumconstantdeclaration = javamm_enumconstantdeclaration;
    }
    public javaMM_AbstractMethodInvocation getJavamm_abstractmethodinvocation() {
        return javamm_abstractmethodinvocation;
    }

    public void setJavamm_abstractmethodinvocation(javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation) {
        this.javamm_abstractmethodinvocation = javamm_abstractmethodinvocation;
    }
    public javaMM_AnnotationTypeMemberDeclaration getJavamm_annotationtypememberdeclaration() {
        return javamm_annotationtypememberdeclaration;
    }

    public void setJavamm_annotationtypememberdeclaration(javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration) {
        this.javamm_annotationtypememberdeclaration = javamm_annotationtypememberdeclaration;
    }

}