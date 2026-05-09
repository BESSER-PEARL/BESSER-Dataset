





import java.util.List;
import java.util.ArrayList;

public class ast_Expression extends ASTNode {






    private ast_PrefixExpression ast_prefixexpression;




    private ast_ConditionalExpression ast_conditionalexpression;




    private ast_InstanceofExpression ast_instanceofexpression;




    private ast_ConditionalExpression ast_conditionalexpression;




    private ast_ConditionalExpression ast_conditionalexpression;




    private ast_ClassInstanceCreation ast_classinstancecreation;




    private ast_MethodInvocation ast_methodinvocation;




    private ast_Assignment ast_assignment;




    private ast_InfixExpression ast_infixexpression;




    private ast_InfixExpression ast_infixexpression;




    private ast_ParenthesizedExpression ast_parenthesizedexpression;




    private ast_SingleMemberAnnotation ast_singlememberannotation;




    private ast_ClassInstanceCreation ast_classinstancecreation;




    private ast_ArrayAccess ast_arrayaccess;




    private ast_FieldAccess ast_fieldaccess;




    private ast_ArrayAccess ast_arrayaccess;




    private ast_InfixExpression ast_infixexpression;




    private ast_CastExpression ast_castexpression;




    private ast_MethodInvocation ast_methodinvocation;




    private ast_ArrayCreation ast_arraycreation;




    private ast_ArrayInitializer ast_arrayinitializer;




    private ast_PostfixExpression ast_postfixexpression;




    private ast_Assignment ast_assignment;




    private ast_SuperMethodInvocation ast_supermethodinvocation;


    public ast_Expression(
    ) {
        super(
        );
    }



    public ast_PrefixExpression getAst_prefixexpression() {
        return ast_prefixexpression;
    }

    public void setAst_prefixexpression(ast_PrefixExpression ast_prefixexpression) {
        this.ast_prefixexpression = ast_prefixexpression;
    }
    public ast_ConditionalExpression getAst_conditionalexpression() {
        return ast_conditionalexpression;
    }

    public void setAst_conditionalexpression(ast_ConditionalExpression ast_conditionalexpression) {
        this.ast_conditionalexpression = ast_conditionalexpression;
    }
    public ast_InstanceofExpression getAst_instanceofexpression() {
        return ast_instanceofexpression;
    }

    public void setAst_instanceofexpression(ast_InstanceofExpression ast_instanceofexpression) {
        this.ast_instanceofexpression = ast_instanceofexpression;
    }
    public ast_ConditionalExpression getAst_conditionalexpression() {
        return ast_conditionalexpression;
    }

    public void setAst_conditionalexpression(ast_ConditionalExpression ast_conditionalexpression) {
        this.ast_conditionalexpression = ast_conditionalexpression;
    }
    public ast_ConditionalExpression getAst_conditionalexpression() {
        return ast_conditionalexpression;
    }

    public void setAst_conditionalexpression(ast_ConditionalExpression ast_conditionalexpression) {
        this.ast_conditionalexpression = ast_conditionalexpression;
    }
    public ast_ClassInstanceCreation getAst_classinstancecreation() {
        return ast_classinstancecreation;
    }

    public void setAst_classinstancecreation(ast_ClassInstanceCreation ast_classinstancecreation) {
        this.ast_classinstancecreation = ast_classinstancecreation;
    }
    public ast_MethodInvocation getAst_methodinvocation() {
        return ast_methodinvocation;
    }

    public void setAst_methodinvocation(ast_MethodInvocation ast_methodinvocation) {
        this.ast_methodinvocation = ast_methodinvocation;
    }
    public ast_Assignment getAst_assignment() {
        return ast_assignment;
    }

    public void setAst_assignment(ast_Assignment ast_assignment) {
        this.ast_assignment = ast_assignment;
    }
    public ast_InfixExpression getAst_infixexpression() {
        return ast_infixexpression;
    }

    public void setAst_infixexpression(ast_InfixExpression ast_infixexpression) {
        this.ast_infixexpression = ast_infixexpression;
    }
    public ast_InfixExpression getAst_infixexpression() {
        return ast_infixexpression;
    }

    public void setAst_infixexpression(ast_InfixExpression ast_infixexpression) {
        this.ast_infixexpression = ast_infixexpression;
    }
    public ast_ParenthesizedExpression getAst_parenthesizedexpression() {
        return ast_parenthesizedexpression;
    }

    public void setAst_parenthesizedexpression(ast_ParenthesizedExpression ast_parenthesizedexpression) {
        this.ast_parenthesizedexpression = ast_parenthesizedexpression;
    }
    public ast_SingleMemberAnnotation getAst_singlememberannotation() {
        return ast_singlememberannotation;
    }

    public void setAst_singlememberannotation(ast_SingleMemberAnnotation ast_singlememberannotation) {
        this.ast_singlememberannotation = ast_singlememberannotation;
    }
    public ast_ClassInstanceCreation getAst_classinstancecreation() {
        return ast_classinstancecreation;
    }

    public void setAst_classinstancecreation(ast_ClassInstanceCreation ast_classinstancecreation) {
        this.ast_classinstancecreation = ast_classinstancecreation;
    }
    public ast_ArrayAccess getAst_arrayaccess() {
        return ast_arrayaccess;
    }

    public void setAst_arrayaccess(ast_ArrayAccess ast_arrayaccess) {
        this.ast_arrayaccess = ast_arrayaccess;
    }
    public ast_FieldAccess getAst_fieldaccess() {
        return ast_fieldaccess;
    }

    public void setAst_fieldaccess(ast_FieldAccess ast_fieldaccess) {
        this.ast_fieldaccess = ast_fieldaccess;
    }
    public ast_ArrayAccess getAst_arrayaccess() {
        return ast_arrayaccess;
    }

    public void setAst_arrayaccess(ast_ArrayAccess ast_arrayaccess) {
        this.ast_arrayaccess = ast_arrayaccess;
    }
    public ast_InfixExpression getAst_infixexpression() {
        return ast_infixexpression;
    }

    public void setAst_infixexpression(ast_InfixExpression ast_infixexpression) {
        this.ast_infixexpression = ast_infixexpression;
    }
    public ast_CastExpression getAst_castexpression() {
        return ast_castexpression;
    }

    public void setAst_castexpression(ast_CastExpression ast_castexpression) {
        this.ast_castexpression = ast_castexpression;
    }
    public ast_MethodInvocation getAst_methodinvocation() {
        return ast_methodinvocation;
    }

    public void setAst_methodinvocation(ast_MethodInvocation ast_methodinvocation) {
        this.ast_methodinvocation = ast_methodinvocation;
    }
    public ast_ArrayCreation getAst_arraycreation() {
        return ast_arraycreation;
    }

    public void setAst_arraycreation(ast_ArrayCreation ast_arraycreation) {
        this.ast_arraycreation = ast_arraycreation;
    }
    public ast_ArrayInitializer getAst_arrayinitializer() {
        return ast_arrayinitializer;
    }

    public void setAst_arrayinitializer(ast_ArrayInitializer ast_arrayinitializer) {
        this.ast_arrayinitializer = ast_arrayinitializer;
    }
    public ast_PostfixExpression getAst_postfixexpression() {
        return ast_postfixexpression;
    }

    public void setAst_postfixexpression(ast_PostfixExpression ast_postfixexpression) {
        this.ast_postfixexpression = ast_postfixexpression;
    }
    public ast_Assignment getAst_assignment() {
        return ast_assignment;
    }

    public void setAst_assignment(ast_Assignment ast_assignment) {
        this.ast_assignment = ast_assignment;
    }
    public ast_SuperMethodInvocation getAst_supermethodinvocation() {
        return ast_supermethodinvocation;
    }

    public void setAst_supermethodinvocation(ast_SuperMethodInvocation ast_supermethodinvocation) {
        this.ast_supermethodinvocation = ast_supermethodinvocation;
    }

}