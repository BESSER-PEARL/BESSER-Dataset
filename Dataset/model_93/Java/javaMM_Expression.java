





import java.util.List;
import java.util.ArrayList;

public class javaMM_Expression extends ASTNode {






    private javaMM_ArrayInitializer javamm_arrayinitializer;




    private javaMM_PostfixExpression javamm_postfixexpression;




    private javaMM_ConditionalExpression javamm_conditionalexpression;




    private javaMM_MethodInvocation javamm_methodinvocation;




    private javaMM_InfixExpression javamm_infixexpression;




    private javaMM_ConditionalExpression javamm_conditionalexpression;




    private javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration;




    private javaMM_SingleVariableAccess javamm_singlevariableaccess;




    private javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation;




    private javaMM_Assignment javamm_assignment;




    private javaMM_ArrayAccess javamm_arrayaccess;




    private javaMM_ArrayLengthAccess javamm_arraylengthaccess;




    private javaMM_ArrayCreation javamm_arraycreation;




    private javaMM_Assignment javamm_assignment;




    private javaMM_FieldAccess javamm_fieldaccess;




    private javaMM_ArrayAccess javamm_arrayaccess;




    private javaMM_CastExpression javamm_castexpression;




    private javaMM_ParenthesizedExpression javamm_parenthesizedexpression;




    private javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration;




    private javaMM_InfixExpression javamm_infixexpression;




    private javaMM_ClassInstanceCreation javamm_classinstancecreation;




    private javaMM_InfixExpression javamm_infixexpression;




    private javaMM_PrefixExpression javamm_prefixexpression;




    private javaMM_InstanceofExpression javamm_instanceofexpression;




    private javaMM_ConditionalExpression javamm_conditionalexpression;


    public javaMM_Expression(
    ) {
        super(
        );
    }



    public javaMM_ArrayInitializer getJavamm_arrayinitializer() {
        return javamm_arrayinitializer;
    }

    public void setJavamm_arrayinitializer(javaMM_ArrayInitializer javamm_arrayinitializer) {
        this.javamm_arrayinitializer = javamm_arrayinitializer;
    }
    public javaMM_PostfixExpression getJavamm_postfixexpression() {
        return javamm_postfixexpression;
    }

    public void setJavamm_postfixexpression(javaMM_PostfixExpression javamm_postfixexpression) {
        this.javamm_postfixexpression = javamm_postfixexpression;
    }
    public javaMM_ConditionalExpression getJavamm_conditionalexpression() {
        return javamm_conditionalexpression;
    }

    public void setJavamm_conditionalexpression(javaMM_ConditionalExpression javamm_conditionalexpression) {
        this.javamm_conditionalexpression = javamm_conditionalexpression;
    }
    public javaMM_MethodInvocation getJavamm_methodinvocation() {
        return javamm_methodinvocation;
    }

    public void setJavamm_methodinvocation(javaMM_MethodInvocation javamm_methodinvocation) {
        this.javamm_methodinvocation = javamm_methodinvocation;
    }
    public javaMM_InfixExpression getJavamm_infixexpression() {
        return javamm_infixexpression;
    }

    public void setJavamm_infixexpression(javaMM_InfixExpression javamm_infixexpression) {
        this.javamm_infixexpression = javamm_infixexpression;
    }
    public javaMM_ConditionalExpression getJavamm_conditionalexpression() {
        return javamm_conditionalexpression;
    }

    public void setJavamm_conditionalexpression(javaMM_ConditionalExpression javamm_conditionalexpression) {
        this.javamm_conditionalexpression = javamm_conditionalexpression;
    }
    public javaMM_EnumConstantDeclaration getJavamm_enumconstantdeclaration() {
        return javamm_enumconstantdeclaration;
    }

    public void setJavamm_enumconstantdeclaration(javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration) {
        this.javamm_enumconstantdeclaration = javamm_enumconstantdeclaration;
    }
    public javaMM_SingleVariableAccess getJavamm_singlevariableaccess() {
        return javamm_singlevariableaccess;
    }

    public void setJavamm_singlevariableaccess(javaMM_SingleVariableAccess javamm_singlevariableaccess) {
        this.javamm_singlevariableaccess = javamm_singlevariableaccess;
    }
    public javaMM_AbstractMethodInvocation getJavamm_abstractmethodinvocation() {
        return javamm_abstractmethodinvocation;
    }

    public void setJavamm_abstractmethodinvocation(javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation) {
        this.javamm_abstractmethodinvocation = javamm_abstractmethodinvocation;
    }
    public javaMM_Assignment getJavamm_assignment() {
        return javamm_assignment;
    }

    public void setJavamm_assignment(javaMM_Assignment javamm_assignment) {
        this.javamm_assignment = javamm_assignment;
    }
    public javaMM_ArrayAccess getJavamm_arrayaccess() {
        return javamm_arrayaccess;
    }

    public void setJavamm_arrayaccess(javaMM_ArrayAccess javamm_arrayaccess) {
        this.javamm_arrayaccess = javamm_arrayaccess;
    }
    public javaMM_ArrayLengthAccess getJavamm_arraylengthaccess() {
        return javamm_arraylengthaccess;
    }

    public void setJavamm_arraylengthaccess(javaMM_ArrayLengthAccess javamm_arraylengthaccess) {
        this.javamm_arraylengthaccess = javamm_arraylengthaccess;
    }
    public javaMM_ArrayCreation getJavamm_arraycreation() {
        return javamm_arraycreation;
    }

    public void setJavamm_arraycreation(javaMM_ArrayCreation javamm_arraycreation) {
        this.javamm_arraycreation = javamm_arraycreation;
    }
    public javaMM_Assignment getJavamm_assignment() {
        return javamm_assignment;
    }

    public void setJavamm_assignment(javaMM_Assignment javamm_assignment) {
        this.javamm_assignment = javamm_assignment;
    }
    public javaMM_FieldAccess getJavamm_fieldaccess() {
        return javamm_fieldaccess;
    }

    public void setJavamm_fieldaccess(javaMM_FieldAccess javamm_fieldaccess) {
        this.javamm_fieldaccess = javamm_fieldaccess;
    }
    public javaMM_ArrayAccess getJavamm_arrayaccess() {
        return javamm_arrayaccess;
    }

    public void setJavamm_arrayaccess(javaMM_ArrayAccess javamm_arrayaccess) {
        this.javamm_arrayaccess = javamm_arrayaccess;
    }
    public javaMM_CastExpression getJavamm_castexpression() {
        return javamm_castexpression;
    }

    public void setJavamm_castexpression(javaMM_CastExpression javamm_castexpression) {
        this.javamm_castexpression = javamm_castexpression;
    }
    public javaMM_ParenthesizedExpression getJavamm_parenthesizedexpression() {
        return javamm_parenthesizedexpression;
    }

    public void setJavamm_parenthesizedexpression(javaMM_ParenthesizedExpression javamm_parenthesizedexpression) {
        this.javamm_parenthesizedexpression = javamm_parenthesizedexpression;
    }
    public javaMM_AnnotationTypeMemberDeclaration getJavamm_annotationtypememberdeclaration() {
        return javamm_annotationtypememberdeclaration;
    }

    public void setJavamm_annotationtypememberdeclaration(javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration) {
        this.javamm_annotationtypememberdeclaration = javamm_annotationtypememberdeclaration;
    }
    public javaMM_InfixExpression getJavamm_infixexpression() {
        return javamm_infixexpression;
    }

    public void setJavamm_infixexpression(javaMM_InfixExpression javamm_infixexpression) {
        this.javamm_infixexpression = javamm_infixexpression;
    }
    public javaMM_ClassInstanceCreation getJavamm_classinstancecreation() {
        return javamm_classinstancecreation;
    }

    public void setJavamm_classinstancecreation(javaMM_ClassInstanceCreation javamm_classinstancecreation) {
        this.javamm_classinstancecreation = javamm_classinstancecreation;
    }
    public javaMM_InfixExpression getJavamm_infixexpression() {
        return javamm_infixexpression;
    }

    public void setJavamm_infixexpression(javaMM_InfixExpression javamm_infixexpression) {
        this.javamm_infixexpression = javamm_infixexpression;
    }
    public javaMM_PrefixExpression getJavamm_prefixexpression() {
        return javamm_prefixexpression;
    }

    public void setJavamm_prefixexpression(javaMM_PrefixExpression javamm_prefixexpression) {
        this.javamm_prefixexpression = javamm_prefixexpression;
    }
    public javaMM_InstanceofExpression getJavamm_instanceofexpression() {
        return javamm_instanceofexpression;
    }

    public void setJavamm_instanceofexpression(javaMM_InstanceofExpression javamm_instanceofexpression) {
        this.javamm_instanceofexpression = javamm_instanceofexpression;
    }
    public javaMM_ConditionalExpression getJavamm_conditionalexpression() {
        return javamm_conditionalexpression;
    }

    public void setJavamm_conditionalexpression(javaMM_ConditionalExpression javamm_conditionalexpression) {
        this.javamm_conditionalexpression = javamm_conditionalexpression;
    }

}