





import java.util.List;
import java.util.ArrayList;

public class ast_MethodDeclaration extends BodyDeclaration {

    private boolean constructor;





    private ast_SimpleName ast_simplename;




    private ast_Block ast_block;




    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private ast_SimpleName ast_simplename;




    private List<ast_SingleVariableDeclaration> ast_singlevariabledeclarations;




    private List<ast_Dimension> ast_dimensions;




    private ast_Type ast_type;




    private List<ast_TypeParameter> ast_typeparameters;




    private List<ast_Type> ast_types;




    private ast_Type ast_type;


    public ast_MethodDeclaration(
        boolean constructor    ) {
        super(
        );
        this.constructor = constructor;
        this.ast_iextendedmodifiers = new ArrayList<>();
        this.ast_singlevariabledeclarations = new ArrayList<>();
        this.ast_dimensions = new ArrayList<>();
        this.ast_typeparameters = new ArrayList<>();
        this.ast_types = new ArrayList<>();
    }

    public ast_MethodDeclaration(
        boolean constructor        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers,        ArrayList<ast_SingleVariableDeclaration> ast_singlevariabledeclarations,        ArrayList<ast_Dimension> ast_dimensions,        ArrayList<ast_TypeParameter> ast_typeparameters,        ArrayList<ast_Type> ast_types    ) {
        this.constructor = constructor;
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
        this.ast_singlevariabledeclarations = ast_singlevariabledeclarations;
        this.ast_dimensions = ast_dimensions;
        this.ast_typeparameters = ast_typeparameters;
        this.ast_types = ast_types;
    }

    public boolean getConstructor() {
        return constructor;
    }

    public void setConstructor(boolean constructor) {
        this.constructor = constructor;
    }

    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public ast_Block getAst_block() {
        return ast_block;
    }

    public void setAst_block(ast_Block ast_block) {
        this.ast_block = ast_block;
    }
    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public List<ast_SingleVariableDeclaration> getAst_singlevariabledeclarations() {
        return ast_singlevariabledeclarations;
    }

    public void addAst_singlevariabledeclaration(Ast_singlevariabledeclaration ast_singlevariabledeclaration) {
        this.ast_singlevariabledeclarations.add(ast_singlevariabledeclaration);
    }
    public List<ast_Dimension> getAst_dimensions() {
        return ast_dimensions;
    }

    public void addAst_dimension(Ast_dimension ast_dimension) {
        this.ast_dimensions.add(ast_dimension);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }
    public List<ast_TypeParameter> getAst_typeparameters() {
        return ast_typeparameters;
    }

    public void addAst_typeparameter(Ast_typeparameter ast_typeparameter) {
        this.ast_typeparameters.add(ast_typeparameter);
    }
    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }

}