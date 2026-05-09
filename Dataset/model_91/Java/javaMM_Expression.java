





import java.util.List;
import java.util.ArrayList;

public class javaMM_Expression extends ASTNode {






    private javaMM_AnnotationTypeMemberDeclaration javamm_annotationtypememberdeclaration;




    private javaMM_InfixExpression javamm_infixexpression;




    private javaMM_PrefixExpression javamm_prefixexpression;




    private javaMM_ConditionalExpression javamm_conditionalexpression;




    private javaMM_ForStatement javamm_forstatement;




    private javaMM_IfStatement javamm_ifstatement;




    private javaMM_ParenthesizedExpression javamm_parenthesizedexpression;




    private javaMM_CastExpression javamm_castexpression;




    private javaMM_ClassInstanceCreation javamm_classinstancecreation;




    private javaMM_InstanceofExpression javamm_instanceofexpression;




    private javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration;




    private javaMM_VariableDeclaration javamm_variabledeclaration;




    private javaMM_SingleVariableAccess javamm_singlevariableaccess;




    private javaMM_ThrowStatement javamm_throwstatement;




    private javaMM_ConditionalExpression javamm_conditionalexpression;




    private javaMM_ForStatement javamm_forstatement;




    private javaMM_MethodInvocation javamm_methodinvocation;




    private javaMM_EnhancedForStatement javamm_enhancedforstatement;




    private javaMM_ForStatement javamm_forstatement;




    private javaMM_DoStatement javamm_dostatement;




    private javaMM_FieldAccess javamm_fieldaccess;




    private javaMM_ExpressionStatement javamm_expressionstatement;




    private javaMM_PostfixExpression javamm_postfixexpression;




    private javaMM_WhileStatement javamm_whilestatement;




    private javaMM_InfixExpression javamm_infixexpression;




    private javaMM_ConditionalExpression javamm_conditionalexpression;




    private javaMM_SwitchStatement javamm_switchstatement;




    private javaMM_SuperConstructorInvocation javamm_superconstructorinvocation;




    private javaMM_SwitchCase javamm_switchcase;




    private javaMM_SynchronizedStatement javamm_synchronizedstatement;




    private javaMM_InfixExpression javamm_infixexpression;




    private javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation;




    private javaMM_ReturnStatement javamm_returnstatement;


    public javaMM_Expression(
    ) {
        super(
        );
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
    public javaMM_PrefixExpression getJavamm_prefixexpression() {
        return javamm_prefixexpression;
    }

    public void setJavamm_prefixexpression(javaMM_PrefixExpression javamm_prefixexpression) {
        this.javamm_prefixexpression = javamm_prefixexpression;
    }
    public javaMM_ConditionalExpression getJavamm_conditionalexpression() {
        return javamm_conditionalexpression;
    }

    public void setJavamm_conditionalexpression(javaMM_ConditionalExpression javamm_conditionalexpression) {
        this.javamm_conditionalexpression = javamm_conditionalexpression;
    }
    public javaMM_ForStatement getJavamm_forstatement() {
        return javamm_forstatement;
    }

    public void setJavamm_forstatement(javaMM_ForStatement javamm_forstatement) {
        this.javamm_forstatement = javamm_forstatement;
    }
    public javaMM_IfStatement getJavamm_ifstatement() {
        return javamm_ifstatement;
    }

    public void setJavamm_ifstatement(javaMM_IfStatement javamm_ifstatement) {
        this.javamm_ifstatement = javamm_ifstatement;
    }
    public javaMM_ParenthesizedExpression getJavamm_parenthesizedexpression() {
        return javamm_parenthesizedexpression;
    }

    public void setJavamm_parenthesizedexpression(javaMM_ParenthesizedExpression javamm_parenthesizedexpression) {
        this.javamm_parenthesizedexpression = javamm_parenthesizedexpression;
    }
    public javaMM_CastExpression getJavamm_castexpression() {
        return javamm_castexpression;
    }

    public void setJavamm_castexpression(javaMM_CastExpression javamm_castexpression) {
        this.javamm_castexpression = javamm_castexpression;
    }
    public javaMM_ClassInstanceCreation getJavamm_classinstancecreation() {
        return javamm_classinstancecreation;
    }

    public void setJavamm_classinstancecreation(javaMM_ClassInstanceCreation javamm_classinstancecreation) {
        this.javamm_classinstancecreation = javamm_classinstancecreation;
    }
    public javaMM_InstanceofExpression getJavamm_instanceofexpression() {
        return javamm_instanceofexpression;
    }

    public void setJavamm_instanceofexpression(javaMM_InstanceofExpression javamm_instanceofexpression) {
        this.javamm_instanceofexpression = javamm_instanceofexpression;
    }
    public javaMM_EnumConstantDeclaration getJavamm_enumconstantdeclaration() {
        return javamm_enumconstantdeclaration;
    }

    public void setJavamm_enumconstantdeclaration(javaMM_EnumConstantDeclaration javamm_enumconstantdeclaration) {
        this.javamm_enumconstantdeclaration = javamm_enumconstantdeclaration;
    }
    public javaMM_VariableDeclaration getJavamm_variabledeclaration() {
        return javamm_variabledeclaration;
    }

    public void setJavamm_variabledeclaration(javaMM_VariableDeclaration javamm_variabledeclaration) {
        this.javamm_variabledeclaration = javamm_variabledeclaration;
    }
    public javaMM_SingleVariableAccess getJavamm_singlevariableaccess() {
        return javamm_singlevariableaccess;
    }

    public void setJavamm_singlevariableaccess(javaMM_SingleVariableAccess javamm_singlevariableaccess) {
        this.javamm_singlevariableaccess = javamm_singlevariableaccess;
    }
    public javaMM_ThrowStatement getJavamm_throwstatement() {
        return javamm_throwstatement;
    }

    public void setJavamm_throwstatement(javaMM_ThrowStatement javamm_throwstatement) {
        this.javamm_throwstatement = javamm_throwstatement;
    }
    public javaMM_ConditionalExpression getJavamm_conditionalexpression() {
        return javamm_conditionalexpression;
    }

    public void setJavamm_conditionalexpression(javaMM_ConditionalExpression javamm_conditionalexpression) {
        this.javamm_conditionalexpression = javamm_conditionalexpression;
    }
    public javaMM_ForStatement getJavamm_forstatement() {
        return javamm_forstatement;
    }

    public void setJavamm_forstatement(javaMM_ForStatement javamm_forstatement) {
        this.javamm_forstatement = javamm_forstatement;
    }
    public javaMM_MethodInvocation getJavamm_methodinvocation() {
        return javamm_methodinvocation;
    }

    public void setJavamm_methodinvocation(javaMM_MethodInvocation javamm_methodinvocation) {
        this.javamm_methodinvocation = javamm_methodinvocation;
    }
    public javaMM_EnhancedForStatement getJavamm_enhancedforstatement() {
        return javamm_enhancedforstatement;
    }

    public void setJavamm_enhancedforstatement(javaMM_EnhancedForStatement javamm_enhancedforstatement) {
        this.javamm_enhancedforstatement = javamm_enhancedforstatement;
    }
    public javaMM_ForStatement getJavamm_forstatement() {
        return javamm_forstatement;
    }

    public void setJavamm_forstatement(javaMM_ForStatement javamm_forstatement) {
        this.javamm_forstatement = javamm_forstatement;
    }
    public javaMM_DoStatement getJavamm_dostatement() {
        return javamm_dostatement;
    }

    public void setJavamm_dostatement(javaMM_DoStatement javamm_dostatement) {
        this.javamm_dostatement = javamm_dostatement;
    }
    public javaMM_FieldAccess getJavamm_fieldaccess() {
        return javamm_fieldaccess;
    }

    public void setJavamm_fieldaccess(javaMM_FieldAccess javamm_fieldaccess) {
        this.javamm_fieldaccess = javamm_fieldaccess;
    }
    public javaMM_ExpressionStatement getJavamm_expressionstatement() {
        return javamm_expressionstatement;
    }

    public void setJavamm_expressionstatement(javaMM_ExpressionStatement javamm_expressionstatement) {
        this.javamm_expressionstatement = javamm_expressionstatement;
    }
    public javaMM_PostfixExpression getJavamm_postfixexpression() {
        return javamm_postfixexpression;
    }

    public void setJavamm_postfixexpression(javaMM_PostfixExpression javamm_postfixexpression) {
        this.javamm_postfixexpression = javamm_postfixexpression;
    }
    public javaMM_WhileStatement getJavamm_whilestatement() {
        return javamm_whilestatement;
    }

    public void setJavamm_whilestatement(javaMM_WhileStatement javamm_whilestatement) {
        this.javamm_whilestatement = javamm_whilestatement;
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
    public javaMM_SwitchStatement getJavamm_switchstatement() {
        return javamm_switchstatement;
    }

    public void setJavamm_switchstatement(javaMM_SwitchStatement javamm_switchstatement) {
        this.javamm_switchstatement = javamm_switchstatement;
    }
    public javaMM_SuperConstructorInvocation getJavamm_superconstructorinvocation() {
        return javamm_superconstructorinvocation;
    }

    public void setJavamm_superconstructorinvocation(javaMM_SuperConstructorInvocation javamm_superconstructorinvocation) {
        this.javamm_superconstructorinvocation = javamm_superconstructorinvocation;
    }
    public javaMM_SwitchCase getJavamm_switchcase() {
        return javamm_switchcase;
    }

    public void setJavamm_switchcase(javaMM_SwitchCase javamm_switchcase) {
        this.javamm_switchcase = javamm_switchcase;
    }
    public javaMM_SynchronizedStatement getJavamm_synchronizedstatement() {
        return javamm_synchronizedstatement;
    }

    public void setJavamm_synchronizedstatement(javaMM_SynchronizedStatement javamm_synchronizedstatement) {
        this.javamm_synchronizedstatement = javamm_synchronizedstatement;
    }
    public javaMM_InfixExpression getJavamm_infixexpression() {
        return javamm_infixexpression;
    }

    public void setJavamm_infixexpression(javaMM_InfixExpression javamm_infixexpression) {
        this.javamm_infixexpression = javamm_infixexpression;
    }
    public javaMM_AbstractMethodInvocation getJavamm_abstractmethodinvocation() {
        return javamm_abstractmethodinvocation;
    }

    public void setJavamm_abstractmethodinvocation(javaMM_AbstractMethodInvocation javamm_abstractmethodinvocation) {
        this.javamm_abstractmethodinvocation = javamm_abstractmethodinvocation;
    }
    public javaMM_ReturnStatement getJavamm_returnstatement() {
        return javamm_returnstatement;
    }

    public void setJavamm_returnstatement(javaMM_ReturnStatement javamm_returnstatement) {
        this.javamm_returnstatement = javamm_returnstatement;
    }

}