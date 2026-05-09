





import java.util.List;
import java.util.ArrayList;

public class DOM_AbstractTypeDeclaration extends BodyDeclaration {

    private String localTypeDeclaration;
    private String packageMemberTypeDeclaration;
    private String memberTypeDeclaration;





    private DOM_CompilationUnit dom_compilationunit;




    private List<DOM_BodyDeclaration> dom_bodydeclarations;


    public DOM_AbstractTypeDeclaration(
        String localTypeDeclaration,        String packageMemberTypeDeclaration,        String memberTypeDeclaration    ) {
        super(
        );
        this.localTypeDeclaration = localTypeDeclaration;
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.memberTypeDeclaration = memberTypeDeclaration;
        this.dom_bodydeclarations = new ArrayList<>();
    }

    public DOM_AbstractTypeDeclaration(
        String localTypeDeclaration,        String packageMemberTypeDeclaration,        String memberTypeDeclaration        ArrayList<DOM_BodyDeclaration> dom_bodydeclarations    ) {
        this.localTypeDeclaration = localTypeDeclaration;
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.memberTypeDeclaration = memberTypeDeclaration;
        this.dom_bodydeclarations = dom_bodydeclarations;
    }

    public String getLocaltypedeclaration() {
        return localTypeDeclaration;
    }

    public void setLocaltypedeclaration(String localTypeDeclaration) {
        this.localTypeDeclaration = localTypeDeclaration;
    }
    public String getPackagemembertypedeclaration() {
        return packageMemberTypeDeclaration;
    }

    public void setPackagemembertypedeclaration(String packageMemberTypeDeclaration) {
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
    }
    public String getMembertypedeclaration() {
        return memberTypeDeclaration;
    }

    public void setMembertypedeclaration(String memberTypeDeclaration) {
        this.memberTypeDeclaration = memberTypeDeclaration;
    }

    public DOM_CompilationUnit getDom_compilationunit() {
        return dom_compilationunit;
    }

    public void setDom_compilationunit(DOM_CompilationUnit dom_compilationunit) {
        this.dom_compilationunit = dom_compilationunit;
    }
    public List<DOM_BodyDeclaration> getDom_bodydeclarations() {
        return dom_bodydeclarations;
    }

    public void addDom_bodydeclaration(Dom_bodydeclaration dom_bodydeclaration) {
        this.dom_bodydeclarations.add(dom_bodydeclaration);
    }

}