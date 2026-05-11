





import java.util.List;
import java.util.ArrayList;

public class miniJava_TypeDeclaration extends NamedElement {

    private String accessLevel;





    private List<miniJava_Member> minijava_members;




    private List<miniJava_Interface> minijava_interfaces;


    public miniJava_TypeDeclaration(
        String accessLevel    ) {
        super(
        );
        this.accessLevel = accessLevel;
        this.minijava_members = new ArrayList<>();
        this.minijava_interfaces = new ArrayList<>();
    }

    public miniJava_TypeDeclaration(
        String accessLevel        ArrayList<miniJava_Member> minijava_members,        ArrayList<miniJava_Interface> minijava_interfaces    ) {
        this.accessLevel = accessLevel;
        this.minijava_members = minijava_members;
        this.minijava_interfaces = minijava_interfaces;
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
    public List<miniJava_Interface> getMinijava_interfaces() {
        return minijava_interfaces;
    }

    public void addMinijava_interface(Minijava_interface minijava_interface) {
        this.minijava_interfaces.add(minijava_interface);
    }

}