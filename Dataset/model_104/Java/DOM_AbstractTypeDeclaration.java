





import java.util.List;
import java.util.ArrayList;

public class DOM_AbstractTypeDeclaration extends BodyDeclaration {

    private String memberTypeDeclaration;
    private String packageMemberTypeDeclaration;
    private String localTypeDeclaration;



    public DOM_AbstractTypeDeclaration(
        String memberTypeDeclaration,        String packageMemberTypeDeclaration,        String localTypeDeclaration    ) {
        super(
        );
        this.memberTypeDeclaration = memberTypeDeclaration;
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.localTypeDeclaration = localTypeDeclaration;
    }


    public String getMembertypedeclaration() {
        return memberTypeDeclaration;
    }

    public void setMembertypedeclaration(String memberTypeDeclaration) {
        this.memberTypeDeclaration = memberTypeDeclaration;
    }
    public String getPackagemembertypedeclaration() {
        return packageMemberTypeDeclaration;
    }

    public void setPackagemembertypedeclaration(String packageMemberTypeDeclaration) {
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
    }
    public String getLocaltypedeclaration() {
        return localTypeDeclaration;
    }

    public void setLocaltypedeclaration(String localTypeDeclaration) {
        this.localTypeDeclaration = localTypeDeclaration;
    }


}