





import java.util.List;
import java.util.ArrayList;

public class DOM_AbstractTypeDeclaration extends BodyDeclaration {

    private String packageMemberTypeDeclaration;
    private String memberTypeDeclaration;
    private String localTypeDeclaration;



    public DOM_AbstractTypeDeclaration(
        String packageMemberTypeDeclaration,        String memberTypeDeclaration,        String localTypeDeclaration    ) {
        super(
        );
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.memberTypeDeclaration = memberTypeDeclaration;
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
    public String getLocaltypedeclaration() {
        return localTypeDeclaration;
    }

    public void setLocaltypedeclaration(String localTypeDeclaration) {
        this.localTypeDeclaration = localTypeDeclaration;
    }


}