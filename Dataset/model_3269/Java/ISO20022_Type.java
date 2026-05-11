





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Type extends RepositoryConcept {






    private List<ISO20022_Member> iso20022_members;




    private ISO20022_Member iso20022_member;


    public ISO20022_Type(
    ) {
        super(
        );
        this.iso20022_members = new ArrayList<>();
    }

    public ISO20022_Type(
        ArrayList<ISO20022_Member> iso20022_members    ) {
        this.iso20022_members = iso20022_members;
    }


    public List<ISO20022_Member> getIso20022_members() {
        return iso20022_members;
    }

    public void addIso20022_member(Iso20022_member iso20022_member) {
        this.iso20022_members.add(iso20022_member);
    }
    public ISO20022_Member getIso20022_member() {
        return iso20022_member;
    }

    public void setIso20022_member(ISO20022_Member iso20022_member) {
        this.iso20022_member = iso20022_member;
    }

}