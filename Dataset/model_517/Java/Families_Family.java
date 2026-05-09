





import java.util.List;
import java.util.ArrayList;

public class Families_Family  {

    private String lastname;





    private List<Families_Member> families_members;




    private Families_Member families_member;




    private Families_Families families_families;




    private Families_Families families_families;


    public Families_Family(
        String lastname    ) {
        this.lastname = lastname;
        this.families_members = new ArrayList<>();
    }

    public Families_Family(
        String lastname        ArrayList<Families_Member> families_members    ) {
        this.lastname = lastname;
        this.families_members = families_members;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public List<Families_Member> getFamilies_members() {
        return families_members;
    }

    public void addFamilies_member(Families_member families_member) {
        this.families_members.add(families_member);
    }
    public Families_Member getFamilies_member() {
        return families_member;
    }

    public void setFamilies_member(Families_Member families_member) {
        this.families_member = families_member;
    }
    public Families_Families getFamilies_families() {
        return families_families;
    }

    public void setFamilies_families(Families_Families families_families) {
        this.families_families = families_families;
    }
    public Families_Families getFamilies_families() {
        return families_families;
    }

    public void setFamilies_families(Families_Families families_families) {
        this.families_families = families_families;
    }

}