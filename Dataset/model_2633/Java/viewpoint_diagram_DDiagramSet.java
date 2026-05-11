





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DDiagramSet  {






    private List<DDiagram> ddiagrams;




    private description_DiagramDescription description_diagramdescription;


    public viewpoint_diagram_DDiagramSet(
    ) {
        this.ddiagrams = new ArrayList<>();
    }

    public viewpoint_diagram_DDiagramSet(
        ArrayList<DDiagram> ddiagrams    ) {
        this.ddiagrams = ddiagrams;
    }


    public List<DDiagram> getDdiagrams() {
        return ddiagrams;
    }

    public void addDdiagram(Ddiagram ddiagram) {
        this.ddiagrams.add(ddiagram);
    }
    public description_DiagramDescription getDescription_diagramdescription() {
        return description_diagramdescription;
    }

    public void setDescription_diagramdescription(description_DiagramDescription description_diagramdescription) {
        this.description_diagramdescription = description_diagramdescription;
    }

}