





import java.util.List;
import java.util.ArrayList;

public class CLASS_System  {

    private String name;





    private CLASS_NamedElement class_namedelement;




    private List<CLASS_NamedElement> class_namedelements;


    public CLASS_System(
        String name    ) {
        this.name = name;
        this.class_namedelements = new ArrayList<>();
    }

    public CLASS_System(
        String name        ArrayList<CLASS_NamedElement> class_namedelements    ) {
        this.name = name;
        this.class_namedelements = class_namedelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CLASS_NamedElement getClass_namedelement() {
        return class_namedelement;
    }

    public void setClass_namedelement(CLASS_NamedElement class_namedelement) {
        this.class_namedelement = class_namedelement;
    }
    public List<CLASS_NamedElement> getClass_namedelements() {
        return class_namedelements;
    }

    public void addClass_namedelement(Class_namedelement class_namedelement) {
        this.class_namedelements.add(class_namedelement);
    }

}