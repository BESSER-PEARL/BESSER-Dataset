





import java.util.List;
import java.util.ArrayList;

public class UML2_Region extends Namespace, RedefinableElement {






    private UML2_State uml2_state;




    private UML2_Vertex uml2_vertex;




    private UML2_Region uml2_region;




    private List<UML2_Vertex> uml2_vertexs;




    private UML2_State uml2_state;


    public UML2_Region(
    ) {
        super(
        );
        this.uml2_vertexs = new ArrayList<>();
    }

    public UML2_Region(
        ArrayList<UML2_Vertex> uml2_vertexs    ) {
        this.uml2_vertexs = uml2_vertexs;
    }


    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }
    public UML2_Vertex getUml2_vertex() {
        return uml2_vertex;
    }

    public void setUml2_vertex(UML2_Vertex uml2_vertex) {
        this.uml2_vertex = uml2_vertex;
    }
    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }
    public List<UML2_Vertex> getUml2_vertexs() {
        return uml2_vertexs;
    }

    public void addUml2_vertex(Uml2_vertex uml2_vertex) {
        this.uml2_vertexs.add(uml2_vertex);
    }
    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }

}