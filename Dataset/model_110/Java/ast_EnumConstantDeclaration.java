





import java.util.List;
import java.util.ArrayList;

public class ast_EnumConstantDeclaration extends BodyDeclaration {






    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_AnonymousClassDeclaration ast_anonymousclassdeclaration;




    private List<ast_Expression> ast_expressions;




    private ast_SimpleName ast_simplename;


    public ast_EnumConstantDeclaration(
    ) {
        super(
        );
        this.ast_iextendedmodifiers = new ArrayList<>();
        this.ast_expressions = new ArrayList<>();
    }

    public ast_EnumConstantDeclaration(
        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers,        ArrayList<ast_Expression> ast_expressions    ) {
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
        this.ast_expressions = ast_expressions;
    }


    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_AnonymousClassDeclaration getAst_anonymousclassdeclaration() {
        return ast_anonymousclassdeclaration;
    }

    public void setAst_anonymousclassdeclaration(ast_AnonymousClassDeclaration ast_anonymousclassdeclaration) {
        this.ast_anonymousclassdeclaration = ast_anonymousclassdeclaration;
    }
    public List<ast_Expression> getAst_expressions() {
        return ast_expressions;
    }

    public void addAst_expression(Ast_expression ast_expression) {
        this.ast_expressions.add(ast_expression);
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}