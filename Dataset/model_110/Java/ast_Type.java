





import java.util.List;
import java.util.ArrayList;

public class ast_Type extends ASTNode {






    private ast_ClassInstanceCreation ast_classinstancecreation;




    private ast_TypeLiteral ast_typeliteral;




    private ast_ClassInstanceCreation ast_classinstancecreation;




    private ast_MethodInvocation ast_methodinvocation;




    private ast_InstanceofExpression ast_instanceofexpression;




    private ast_CastExpression ast_castexpression;




    private ast_VariableDeclarationExpression ast_variabledeclarationexpression;




    private ast_TypeParameter ast_typeparameter;




    private ast_MethodRefParameter ast_methodrefparameter;




    private ast_SuperMethodInvocation ast_supermethodinvocation;


    public ast_Type(
    ) {
        super(
        );
    }



    public ast_ClassInstanceCreation getAst_classinstancecreation() {
        return ast_classinstancecreation;
    }

    public void setAst_classinstancecreation(ast_ClassInstanceCreation ast_classinstancecreation) {
        this.ast_classinstancecreation = ast_classinstancecreation;
    }
    public ast_TypeLiteral getAst_typeliteral() {
        return ast_typeliteral;
    }

    public void setAst_typeliteral(ast_TypeLiteral ast_typeliteral) {
        this.ast_typeliteral = ast_typeliteral;
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
    public ast_InstanceofExpression getAst_instanceofexpression() {
        return ast_instanceofexpression;
    }

    public void setAst_instanceofexpression(ast_InstanceofExpression ast_instanceofexpression) {
        this.ast_instanceofexpression = ast_instanceofexpression;
    }
    public ast_CastExpression getAst_castexpression() {
        return ast_castexpression;
    }

    public void setAst_castexpression(ast_CastExpression ast_castexpression) {
        this.ast_castexpression = ast_castexpression;
    }
    public ast_VariableDeclarationExpression getAst_variabledeclarationexpression() {
        return ast_variabledeclarationexpression;
    }

    public void setAst_variabledeclarationexpression(ast_VariableDeclarationExpression ast_variabledeclarationexpression) {
        this.ast_variabledeclarationexpression = ast_variabledeclarationexpression;
    }
    public ast_TypeParameter getAst_typeparameter() {
        return ast_typeparameter;
    }

    public void setAst_typeparameter(ast_TypeParameter ast_typeparameter) {
        this.ast_typeparameter = ast_typeparameter;
    }
    public ast_MethodRefParameter getAst_methodrefparameter() {
        return ast_methodrefparameter;
    }

    public void setAst_methodrefparameter(ast_MethodRefParameter ast_methodrefparameter) {
        this.ast_methodrefparameter = ast_methodrefparameter;
    }
    public ast_SuperMethodInvocation getAst_supermethodinvocation() {
        return ast_supermethodinvocation;
    }

    public void setAst_supermethodinvocation(ast_SuperMethodInvocation ast_supermethodinvocation) {
        this.ast_supermethodinvocation = ast_supermethodinvocation;
    }

}