





import java.util.List;
import java.util.ArrayList;

public class uma_Diagram extends GraphNode {

    private String zoom;





    private uma_Point uma_point;




    private uma_SemanticModelBridge uma_semanticmodelbridge;




    private uma_ProcessPackage uma_processpackage;




    private List<uma_DiagramLink> uma_diagramlinks;




    private uma_SemanticModelBridge uma_semanticmodelbridge;




    private uma_DiagramLink uma_diagramlink;


    public uma_Diagram(
        String zoom    ) {
        super(
        );
        this.zoom = zoom;
        this.uma_diagramlinks = new ArrayList<>();
    }

    public uma_Diagram(
        String zoom        ArrayList<uma_DiagramLink> uma_diagramlinks    ) {
        this.zoom = zoom;
        this.uma_diagramlinks = uma_diagramlinks;
    }

    public String getZoom() {
        return zoom;
    }

    public void setZoom(String zoom) {
        this.zoom = zoom;
    }

    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }
    public uma_SemanticModelBridge getUma_semanticmodelbridge() {
        return uma_semanticmodelbridge;
    }

    public void setUma_semanticmodelbridge(uma_SemanticModelBridge uma_semanticmodelbridge) {
        this.uma_semanticmodelbridge = uma_semanticmodelbridge;
    }
    public uma_ProcessPackage getUma_processpackage() {
        return uma_processpackage;
    }

    public void setUma_processpackage(uma_ProcessPackage uma_processpackage) {
        this.uma_processpackage = uma_processpackage;
    }
    public List<uma_DiagramLink> getUma_diagramlinks() {
        return uma_diagramlinks;
    }

    public void addUma_diagramlink(Uma_diagramlink uma_diagramlink) {
        this.uma_diagramlinks.add(uma_diagramlink);
    }
    public uma_SemanticModelBridge getUma_semanticmodelbridge() {
        return uma_semanticmodelbridge;
    }

    public void setUma_semanticmodelbridge(uma_SemanticModelBridge uma_semanticmodelbridge) {
        this.uma_semanticmodelbridge = uma_semanticmodelbridge;
    }
    public uma_DiagramLink getUma_diagramlink() {
        return uma_diagramlink;
    }

    public void setUma_diagramlink(uma_DiagramLink uma_diagramlink) {
        this.uma_diagramlink = uma_diagramlink;
    }

}