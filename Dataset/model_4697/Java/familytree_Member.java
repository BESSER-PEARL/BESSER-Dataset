





import java.util.List;
import java.util.ArrayList;

public class familytree_Member  {

    private String name;
    private int age;





    private List<familytree_Member> familytree_members;




    private familytree_Member familytree_member;


    public familytree_Member(
        String name,        int age    ) {
        this.name = name;
        this.age = age;
        this.familytree_members = new ArrayList<>();
    }

    public familytree_Member(
        String name,        int age        ArrayList<familytree_Member> familytree_members    ) {
        this.name = name;
        this.age = age;
        this.familytree_members = familytree_members;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public List<familytree_Member> getFamilytree_members() {
        return familytree_members;
    }

    public void addFamilytree_member(Familytree_member familytree_member) {
        this.familytree_members.add(familytree_member);
    }
    public familytree_Member getFamilytree_member() {
        return familytree_member;
    }

    public void setFamilytree_member(familytree_Member familytree_member) {
        this.familytree_member = familytree_member;
    }

}