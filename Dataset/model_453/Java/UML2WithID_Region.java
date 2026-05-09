





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Region extends RedefinableElement, Namespace {






    private UML2WithID_StateMachine uml2withid_statemachine;




    private UML2WithID_StateMachine uml2withid_statemachine;




    private UML2WithID_State uml2withid_state;




    private List<UML2WithID_Vertex> uml2withid_vertexs;




    private UML2WithID_State uml2withid_state;




    private UML2WithID_Vertex uml2withid_vertex;




    private UML2WithID_Region uml2withid_region;


    public UML2WithID_Region(
    ) {
        super(
        );
        this.uml2withid_vertexs = new ArrayList<>();
    }

    public UML2WithID_Region(
        ArrayList<UML2WithID_Vertex> uml2withid_vertexs    ) {
        this.uml2withid_vertexs = uml2withid_vertexs;
    }


    public UML2WithID_StateMachine getUml2withid_statemachine() {
        return uml2withid_statemachine;
    }

    public void setUml2withid_statemachine(UML2WithID_StateMachine uml2withid_statemachine) {
        this.uml2withid_statemachine = uml2withid_statemachine;
    }
    public UML2WithID_StateMachine getUml2withid_statemachine() {
        return uml2withid_statemachine;
    }

    public void setUml2withid_statemachine(UML2WithID_StateMachine uml2withid_statemachine) {
        this.uml2withid_statemachine = uml2withid_statemachine;
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public List<UML2WithID_Vertex> getUml2withid_vertexs() {
        return uml2withid_vertexs;
    }

    public void addUml2withid_vertex(Uml2withid_vertex uml2withid_vertex) {
        this.uml2withid_vertexs.add(uml2withid_vertex);
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public UML2WithID_Vertex getUml2withid_vertex() {
        return uml2withid_vertex;
    }

    public void setUml2withid_vertex(UML2WithID_Vertex uml2withid_vertex) {
        this.uml2withid_vertex = uml2withid_vertex;
    }
    public UML2WithID_Region getUml2withid_region() {
        return uml2withid_region;
    }

    public void setUml2withid_region(UML2WithID_Region uml2withid_region) {
        this.uml2withid_region = uml2withid_region;
    }

}