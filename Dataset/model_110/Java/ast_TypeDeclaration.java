





import java.util.List;
import java.util.ArrayList;

public class ast_TypeDeclaration extends AbstractTypeDeclaration {

    private boolean interface;





    private ast_SimpleName ast_simplename;




    private ast_Javadoc ast_javadoc;




    private ast_Type ast_type;




    private List<ast_IExtendedModifier> ast_iextendedmodifiers;




    private List<ast_BodyDeclaration> ast_bodydeclarations;




    private List<ast_TypeParameter> ast_typeparameters;




    private List<ast_Type> ast_types;


    public ast_TypeDeclaration(
        boolean interface    ) {
        super(
        );
        this.interface = interface;
        this.ast_iextendedmodifiers = new ArrayList<>();
        this.ast_bodydeclarations = new ArrayList<>();
        this.ast_typeparameters = new ArrayList<>();
        this.ast_types = new ArrayList<>();
    }

    public ast_TypeDeclaration(
        boolean interface        ArrayList<ast_IExtendedModifier> ast_iextendedmodifiers,        ArrayList<ast_BodyDeclaration> ast_bodydeclarations,        ArrayList<ast_TypeParameter> ast_typeparameters,        ArrayList<ast_Type> ast_types    ) {
        this.interface = interface;
        this.ast_iextendedmodifiers = ast_iextendedmodifiers;
        this.ast_bodydeclarations = ast_bodydeclarations;
        this.ast_typeparameters = ast_typeparameters;
        this.ast_types = ast_types;
    }

    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }

    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }
    public ast_Javadoc getAst_javadoc() {
        return ast_javadoc;
    }

    public void setAst_javadoc(ast_Javadoc ast_javadoc) {
        this.ast_javadoc = ast_javadoc;
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }
    public List<ast_IExtendedModifier> getAst_iextendedmodifiers() {
        return ast_iextendedmodifiers;
    }

    public void addAst_iextendedmodifier(Ast_iextendedmodifier ast_iextendedmodifier) {
        this.ast_iextendedmodifiers.add(ast_iextendedmodifier);
    }
    public List<ast_BodyDeclaration> getAst_bodydeclarations() {
        return ast_bodydeclarations;
    }

    public void addAst_bodydeclaration(Ast_bodydeclaration ast_bodydeclaration) {
        this.ast_bodydeclarations.add(ast_bodydeclaration);
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

}