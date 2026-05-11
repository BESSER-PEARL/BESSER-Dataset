





import java.util.List;
import java.util.ArrayList;

public class mtm_di_Plane extends Node {

    private String diagramElementGroup;





    private List<mtm_di_DiagramElement> mtm_di_diagramelements;


    public mtm_di_Plane(
        String diagramElementGroup    ) {
        super(
        );
        this.diagramElementGroup = diagramElementGroup;
        this.mtm_di_diagramelements = new ArrayList<>();
    }

    public mtm_di_Plane(
        String diagramElementGroup        ArrayList<mtm_di_DiagramElement> mtm_di_diagramelements    ) {
        this.diagramElementGroup = diagramElementGroup;
        this.mtm_di_diagramelements = mtm_di_diagramelements;
    }

    public String getDiagramelementgroup() {
        return diagramElementGroup;
    }

    public void setDiagramelementgroup(String diagramElementGroup) {
        this.diagramElementGroup = diagramElementGroup;
    }

    public List<mtm_di_DiagramElement> getMtm_di_diagramelements() {
        return mtm_di_diagramelements;
    }

    public void addMtm_di_diagramelement(Mtm_di_diagramelement mtm_di_diagramelement) {
        this.mtm_di_diagramelements.add(mtm_di_diagramelement);
    }

}