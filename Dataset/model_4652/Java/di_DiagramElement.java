





import java.util.List;
import java.util.ArrayList;

public class di_DiagramElement  {

    private String id;





    private di_Edge di_edge;




    private di_Edge di_edge;




    private di_DiagramElement di_diagramelement;




    private di_DiagramElement di_diagramelement;




    private List<di_EObject> di_eobjects;


    public di_DiagramElement(
        String id    ) {
        this.id = id;
        this.di_eobjects = new ArrayList<>();
    }

    public di_DiagramElement(
        String id        ArrayList<di_EObject> di_eobjects    ) {
        this.id = id;
        this.di_eobjects = di_eobjects;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public di_Edge getDi_edge() {
        return di_edge;
    }

    public void setDi_edge(di_Edge di_edge) {
        this.di_edge = di_edge;
    }
    public di_Edge getDi_edge() {
        return di_edge;
    }

    public void setDi_edge(di_Edge di_edge) {
        this.di_edge = di_edge;
    }
    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }
    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }
    public List<di_EObject> getDi_eobjects() {
        return di_eobjects;
    }

    public void addDi_eobject(Di_eobject di_eobject) {
        this.di_eobjects.add(di_eobject);
    }

}