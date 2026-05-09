





import java.util.List;
import java.util.ArrayList;

public class families_FamilyModel  {






    private families_Member families_member;




    private List<families_Member> families_members;




    private List<families_Family> families_familys;




    private families_Family families_family;


    public families_FamilyModel(
    ) {
        this.families_members = new ArrayList<>();
        this.families_familys = new ArrayList<>();
    }

    public families_FamilyModel(
        ArrayList<families_Member> families_members,        ArrayList<families_Family> families_familys    ) {
        this.families_members = families_members;
        this.families_familys = families_familys;
    }


    public families_Member getFamilies_member() {
        return families_member;
    }

    public void setFamilies_member(families_Member families_member) {
        this.families_member = families_member;
    }
    public List<families_Member> getFamilies_members() {
        return families_members;
    }

    public void addFamilies_member(Families_member families_member) {
        this.families_members.add(families_member);
    }
    public List<families_Family> getFamilies_familys() {
        return families_familys;
    }

    public void addFamilies_family(Families_family families_family) {
        this.families_familys.add(families_family);
    }
    public families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(families_Family families_family) {
        this.families_family = families_family;
    }

}