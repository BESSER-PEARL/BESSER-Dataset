





import java.util.List;
import java.util.ArrayList;

public class miniJava_TypeDeclaration extends NamedElement {

    private String accessLevel;





    private List<miniJava_Member> minijava_members;




    private miniJava_Program minijava_program;


    public miniJava_TypeDeclaration(
        String accessLevel    ) {
        super(
        );
        this.accessLevel = accessLevel;
        this.minijava_members = new ArrayList<>();
    }

    public miniJava_TypeDeclaration(
        String accessLevel        ArrayList<miniJava_Member> minijava_members    ) {
        this.accessLevel = accessLevel;
        this.minijava_members = minijava_members;
    }

    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }

    public List<miniJava_Member> getMinijava_members() {
        return minijava_members;
    }

    public void addMinijava_member(Minijava_member minijava_member) {
        this.minijava_members.add(minijava_member);
    }
    public miniJava_Program getMinijava_program() {
        return minijava_program;
    }

    public void setMinijava_program(miniJava_Program minijava_program) {
        this.minijava_program = minijava_program;
    }

}