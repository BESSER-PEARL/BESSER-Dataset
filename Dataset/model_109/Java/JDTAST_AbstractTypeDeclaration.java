





import java.util.List;
import java.util.ArrayList;

public class JDTAST_AbstractTypeDeclaration extends BodyDeclaration {

    private String localTypeDeclaration;
    private String packageMemberTypeDeclaration;
    private String memberTypeDeclaration;





    private JDTAST_CompilationUnit jdtast_compilationunit;




    private List<JDTAST_BodyDeclaration> jdtast_bodydeclarations;


    public JDTAST_AbstractTypeDeclaration(
        String localTypeDeclaration,        String packageMemberTypeDeclaration,        String memberTypeDeclaration    ) {
        super(
        );
        this.localTypeDeclaration = localTypeDeclaration;
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.memberTypeDeclaration = memberTypeDeclaration;
        this.jdtast_bodydeclarations = new ArrayList<>();
    }

    public JDTAST_AbstractTypeDeclaration(
        String localTypeDeclaration,        String packageMemberTypeDeclaration,        String memberTypeDeclaration        ArrayList<JDTAST_BodyDeclaration> jdtast_bodydeclarations    ) {
        this.localTypeDeclaration = localTypeDeclaration;
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.memberTypeDeclaration = memberTypeDeclaration;
        this.jdtast_bodydeclarations = jdtast_bodydeclarations;
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

    public JDTAST_CompilationUnit getJdtast_compilationunit() {
        return jdtast_compilationunit;
    }

    public void setJdtast_compilationunit(JDTAST_CompilationUnit jdtast_compilationunit) {
        this.jdtast_compilationunit = jdtast_compilationunit;
    }
    public List<JDTAST_BodyDeclaration> getJdtast_bodydeclarations() {
        return jdtast_bodydeclarations;
    }

    public void addJdtast_bodydeclaration(Jdtast_bodydeclaration jdtast_bodydeclaration) {
        this.jdtast_bodydeclarations.add(jdtast_bodydeclaration);
    }

}