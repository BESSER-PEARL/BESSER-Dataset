





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_CollaborationOccurrence extends NamedElement {






    private List<UML2WithID_Dependency> uml2withid_dependencys;


    public UML2WithID_CollaborationOccurrence(
    ) {
        super(
        );
        this.uml2withid_dependencys = new ArrayList<>();
    }

    public UML2WithID_CollaborationOccurrence(
        ArrayList<UML2WithID_Dependency> uml2withid_dependencys    ) {
        this.uml2withid_dependencys = uml2withid_dependencys;
    }


    public List<UML2WithID_Dependency> getUml2withid_dependencys() {
        return uml2withid_dependencys;
    }

    public void addUml2withid_dependency(Uml2withid_dependency uml2withid_dependency) {
        this.uml2withid_dependencys.add(uml2withid_dependency);
    }

}