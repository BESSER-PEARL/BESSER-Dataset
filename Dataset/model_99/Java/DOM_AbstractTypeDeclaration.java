





import java.util.List;
import java.util.ArrayList;

public class DOM_AbstractTypeDeclaration extends BodyDeclaration {

    private String packageMemberTypeDeclaration;
    private String localTypeDeclaration;
    private String memberTypeDeclaration;



    public DOM_AbstractTypeDeclaration(
        String packageMemberTypeDeclaration,        String localTypeDeclaration,        String memberTypeDeclaration    ) {
        super(
        );
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
        this.localTypeDeclaration = localTypeDeclaration;
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
    public String getMembertypedeclaration() {
        return memberTypeDeclaration;
    }

    public void setMembertypedeclaration(String memberTypeDeclaration) {
        this.memberTypeDeclaration = memberTypeDeclaration;
    }


}