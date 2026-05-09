





import java.util.List;
import java.util.ArrayList;

public class ast_Javadoc extends Comment {






    private ast_PackageDeclaration ast_packagedeclaration;




    private ast_AnnotationTypeMemberDeclaration ast_annotationtypememberdeclaration;




    private ast_Initializer ast_initializer;




    private ast_FieldDeclaration ast_fielddeclaration;




    private ast_MethodDeclaration ast_methoddeclaration;




    private ast_EnumConstantDeclaration ast_enumconstantdeclaration;




    private List<ast_TagElement> ast_tagelements;


    public ast_Javadoc(
    ) {
        super(
        );
        this.ast_tagelements = new ArrayList<>();
    }

    public ast_Javadoc(
        ArrayList<ast_TagElement> ast_tagelements    ) {
        this.ast_tagelements = ast_tagelements;
    }


    public ast_PackageDeclaration getAst_packagedeclaration() {
        return ast_packagedeclaration;
    }

    public void setAst_packagedeclaration(ast_PackageDeclaration ast_packagedeclaration) {
        this.ast_packagedeclaration = ast_packagedeclaration;
    }
    public ast_AnnotationTypeMemberDeclaration getAst_annotationtypememberdeclaration() {
        return ast_annotationtypememberdeclaration;
    }

    public void setAst_annotationtypememberdeclaration(ast_AnnotationTypeMemberDeclaration ast_annotationtypememberdeclaration) {
        this.ast_annotationtypememberdeclaration = ast_annotationtypememberdeclaration;
    }
    public ast_Initializer getAst_initializer() {
        return ast_initializer;
    }

    public void setAst_initializer(ast_Initializer ast_initializer) {
        this.ast_initializer = ast_initializer;
    }
    public ast_FieldDeclaration getAst_fielddeclaration() {
        return ast_fielddeclaration;
    }

    public void setAst_fielddeclaration(ast_FieldDeclaration ast_fielddeclaration) {
        this.ast_fielddeclaration = ast_fielddeclaration;
    }
    public ast_MethodDeclaration getAst_methoddeclaration() {
        return ast_methoddeclaration;
    }

    public void setAst_methoddeclaration(ast_MethodDeclaration ast_methoddeclaration) {
        this.ast_methoddeclaration = ast_methoddeclaration;
    }
    public ast_EnumConstantDeclaration getAst_enumconstantdeclaration() {
        return ast_enumconstantdeclaration;
    }

    public void setAst_enumconstantdeclaration(ast_EnumConstantDeclaration ast_enumconstantdeclaration) {
        this.ast_enumconstantdeclaration = ast_enumconstantdeclaration;
    }
    public List<ast_TagElement> getAst_tagelements() {
        return ast_tagelements;
    }

    public void addAst_tagelement(Ast_tagelement ast_tagelement) {
        this.ast_tagelements.add(ast_tagelement);
    }

}