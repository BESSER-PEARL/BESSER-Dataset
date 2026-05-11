





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedCollaborationUse extends TracedNamedElement {






    private uml_TracedCollaboration uml_tracedcollaboration;




    private List<uml_TracedDependency> uml_traceddependencys;


    public umlTrace_uml_TracedCollaborationUse(
    ) {
        super(
        );
        this.uml_traceddependencys = new ArrayList<>();
    }

    public umlTrace_uml_TracedCollaborationUse(
        ArrayList<uml_TracedDependency> uml_traceddependencys    ) {
        this.uml_traceddependencys = uml_traceddependencys;
    }


    public uml_TracedCollaboration getUml_tracedcollaboration() {
        return uml_tracedcollaboration;
    }

    public void setUml_tracedcollaboration(uml_TracedCollaboration uml_tracedcollaboration) {
        this.uml_tracedcollaboration = uml_tracedcollaboration;
    }
    public List<uml_TracedDependency> getUml_traceddependencys() {
        return uml_traceddependencys;
    }

    public void addUml_traceddependency(Uml_traceddependency uml_traceddependency) {
        this.uml_traceddependencys.add(uml_traceddependency);
    }

}