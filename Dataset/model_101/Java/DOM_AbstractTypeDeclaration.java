





import java.util.List;
import java.util.ArrayList;

public class DOM_AbstractTypeDeclaration extends BodyDeclaration {

    private String localTypeDeclaration;
    private String memberTypeDeclaration;
    private String packageMemberTypeDeclaration;



    public DOM_AbstractTypeDeclaration(
        String localTypeDeclaration,        String memberTypeDeclaration,        String packageMemberTypeDeclaration    ) {
        super(
        );
        this.localTypeDeclaration = localTypeDeclaration;
        this.memberTypeDeclaration = memberTypeDeclaration;
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
    public String getPackagemembertypedeclaration() {
        return packageMemberTypeDeclaration;
    }

    public void setPackagemembertypedeclaration(String packageMemberTypeDeclaration) {
        this.packageMemberTypeDeclaration = packageMemberTypeDeclaration;
    }


}