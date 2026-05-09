





import java.util.List;
import java.util.ArrayList;

public class ast_AnnotationTypeMemberDeclaration extends BodyDeclaration {






    private ast_Expression ast_expression;




    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_Type ast_type;




    private ast_SimpleName ast_simplename;


    public ast_AnnotationTypeMemberDeclaration(
    ) {
        super(
        );
        this.ast_iextendedmodifiers = new ArrayList<>();
    }

    public ast_AnnotationTypeMemberDeclaration(
        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers    ) {
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
    }


    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}