





import java.util.List;
import java.util.ArrayList;

public class UML2_ActivityGroup extends Element {






    private UML2_ActivityNode uml2_activitynode;




    private UML2_ActivityEdge uml2_activityedge;




    private UML2_ActivityGroup uml2_activitygroup;


    public UML2_ActivityGroup(
    ) {
        super(
        );
    }



    public UML2_ActivityNode getUml2_activitynode() {
        return uml2_activitynode;
    }

    public void setUml2_activitynode(UML2_ActivityNode uml2_activitynode) {
        this.uml2_activitynode = uml2_activitynode;
    }
    public UML2_ActivityEdge getUml2_activityedge() {
        return uml2_activityedge;
    }

    public void setUml2_activityedge(UML2_ActivityEdge uml2_activityedge) {
        this.uml2_activityedge = uml2_activityedge;
    }
    public UML2_ActivityGroup getUml2_activitygroup() {
        return uml2_activitygroup;
    }

    public void setUml2_activitygroup(UML2_ActivityGroup uml2_activitygroup) {
        this.uml2_activitygroup = uml2_activitygroup;
    }

}