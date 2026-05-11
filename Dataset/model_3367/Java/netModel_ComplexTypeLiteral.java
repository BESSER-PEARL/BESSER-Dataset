





import java.util.List;
import java.util.ArrayList;

public class netModel_ComplexTypeLiteral extends BlockType {






    private netModel_ComplexTypeDeclaration netmodel_complextypedeclaration;




    private netModel_SkipMember netmodel_skipmember;




    private List<netModel_Member> netmodel_members;


    public netModel_ComplexTypeLiteral(
    ) {
        super(
        );
        this.netmodel_members = new ArrayList<>();
    }

    public netModel_ComplexTypeLiteral(
        ArrayList<netModel_Member> netmodel_members    ) {
        this.netmodel_members = netmodel_members;
    }


    public netModel_ComplexTypeDeclaration getNetmodel_complextypedeclaration() {
        return netmodel_complextypedeclaration;
    }

    public void setNetmodel_complextypedeclaration(netModel_ComplexTypeDeclaration netmodel_complextypedeclaration) {
        this.netmodel_complextypedeclaration = netmodel_complextypedeclaration;
    }
    public netModel_SkipMember getNetmodel_skipmember() {
        return netmodel_skipmember;
    }

    public void setNetmodel_skipmember(netModel_SkipMember netmodel_skipmember) {
        this.netmodel_skipmember = netmodel_skipmember;
    }
    public List<netModel_Member> getNetmodel_members() {
        return netmodel_members;
    }

    public void addNetmodel_member(Netmodel_member netmodel_member) {
        this.netmodel_members.add(netmodel_member);
    }

}