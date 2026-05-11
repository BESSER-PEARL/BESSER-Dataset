





import java.util.List;
import java.util.ArrayList;

public class familytree_FamilyTree  {






    private List<familytree_Member> familytree_members;


    public familytree_FamilyTree(
    ) {
        this.familytree_members = new ArrayList<>();
    }

    public familytree_FamilyTree(
        ArrayList<familytree_Member> familytree_members    ) {
        this.familytree_members = familytree_members;
    }


    public List<familytree_Member> getFamilytree_members() {
        return familytree_members;
    }

    public void addFamilytree_member(Familytree_member familytree_member) {
        this.familytree_members.add(familytree_member);
    }

}