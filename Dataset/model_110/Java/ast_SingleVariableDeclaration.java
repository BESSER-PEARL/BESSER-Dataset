





import java.util.List;
import java.util.ArrayList;

public class ast_SingleVariableDeclaration extends VariableDeclaration {

    private boolean varargs;





    private ast_Type ast_type;




    private ast_Expression ast_expression;




    private ast_CatchClause ast_catchclause;




    private ast_EnhancedForStatement ast_enhancedforstatement;




    private List<ast_Annotation> ast_annotations;




    private ast_SimpleName ast_simplename;




    private List<ast_Dimension> ast_dimensions;




    private List<ast_IExtendedModifier> ast_iextendedmodifiers;


    public ast_SingleVariableDeclaration(
        boolean varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.ast_annotations = new ArrayList<>();
        this.ast_dimensions = new ArrayList<>();
        this.ast_iextendedmodifiers = new ArrayList<>();
    }

    public ast_SingleVariableDeclaration(
        boolean varargs        ArrayList<ast_Annotation> ast_annotations,        ArrayList<ast_Dimension> ast_dimensions,        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers    ) {
        this.varargs = varargs;
        this.ast_annotations = ast_annotations;
        this.ast_dimensions = ast_dimensions;
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
    }

    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }

    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }
    public ast_CatchClause getAst_catchclause() {
        return ast_catchclause;
    }

    public void setAst_catchclause(ast_CatchClause ast_catchclause) {
        this.ast_catchclause = ast_catchclause;
    }
    public ast_EnhancedForStatement getAst_enhancedforstatement() {
        return ast_enhancedforstatement;
    }

    public void setAst_enhancedforstatement(ast_EnhancedForStatement ast_enhancedforstatement) {
        this.ast_enhancedforstatement = ast_enhancedforstatement;
    }
    public List<ast_Annotation> getAst_annotations() {
        return ast_annotations;
    }

    public void addAst_annotation(Ast_annotation ast_annotation) {
        this.ast_annotations.add(ast_annotation);
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public List<ast_Dimension> getAst_dimensions() {
        return ast_dimensions;
    }

    public void addAst_dimension(Ast_dimension ast_dimension) {
        this.ast_dimensions.add(ast_dimension);
    }
    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }

}