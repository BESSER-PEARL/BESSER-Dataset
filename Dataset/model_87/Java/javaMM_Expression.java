





import java.util.List;
import java.util.ArrayList;

public class javaMM_Expression extends ASTNode {






    private javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration;




    private javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation;




    private javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration;




    private javaMM_VariableDeclaration javamm_variabledeclaration;




    private javaMM_AnnotationMemberValuePair javamm_annotationmembervaluepair;


    public javaMM_Expression(
    ) {
        super(
        );
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
    public javaMM_VariableDeclaration getJavamm_variabledeclaration() {
        return javamm_variabledeclaration;
    }

    public void setJavamm_variabledeclaration(javaMM_VariableDeclaration javamm_variabledeclaration) {
        this.javamm_variabledeclaration = javamm_variabledeclaration;
    }
    public javaMM_AnnotationMemberValuePair getJavamm_annotationmembervaluepair() {
        return javamm_annotationmembervaluepair;
    }

    public void setJavamm_annotationmembervaluepair(javaMM_AnnotationMemberValuePair javamm_annotationmembervaluepair) {
        this.javamm_annotationmembervaluepair = javamm_annotationmembervaluepair;
    }

}