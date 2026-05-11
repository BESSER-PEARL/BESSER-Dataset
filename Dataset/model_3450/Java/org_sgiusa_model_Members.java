





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Members  {






    private List<Member> members;


    public org_sgiusa_model_Members(
    ) {
        this.members = new ArrayList<>();
    }

    public org_sgiusa_model_Members(
        ArrayList<Member> members    ) {
        this.members = members;
    }


    public List<Member> getMembers() {
        return members;
    }

    public void addMember(Member member) {
        this.members.add(member);
    }

}