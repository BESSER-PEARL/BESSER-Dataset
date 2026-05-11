





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DDiagramElementContainer extends diagram_EdgeTarget, DContainer, DragAndDropTarget, diagram_AbstractDNode {

    private String width;
    private String height;





    private List<DDiagramElement> ddiagramelements;


    public viewpoint_diagram_DDiagramElementContainer(
        String width,        String height    ) {
        super(
        );
        this.width = width;
        this.height = height;
        this.ddiagramelements = new ArrayList<>();
    }

    public viewpoint_diagram_DDiagramElementContainer(
        String width,        String height        ArrayList<DDiagramElement> ddiagramelements    ) {
        this.width = width;
        this.height = height;
        this.ddiagramelements = ddiagramelements;
    }

    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public List<DDiagramElement> getDdiagramelements() {
        return ddiagramelements;
    }

    public void addDdiagramelement(Ddiagramelement ddiagramelement) {
        this.ddiagramelements.add(ddiagramelement);
    }

}