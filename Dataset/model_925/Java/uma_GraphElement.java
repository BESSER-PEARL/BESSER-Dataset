





import java.util.List;
import java.util.ArrayList;

public class uma_GraphElement extends DiagramElement {






    private uma_GraphConnector uma_graphconnector;




    private uma_DiagramLink uma_diagramlink;




    private uma_SemanticModelBridge uma_semanticmodelbridge;




    private uma_SemanticModelBridge uma_semanticmodelbridge;




    private List<uma_DiagramLink> uma_diagramlinks;




    private List<uma_GraphConnector> uma_graphconnectors;




    private uma_Point uma_point;


    public uma_GraphElement(
    ) {
        super(
        );
        this.uma_diagramlinks = new ArrayList<>();
        this.uma_graphconnectors = new ArrayList<>();
    }

    public uma_GraphElement(
        ArrayList<uma_DiagramLink> uma_diagramlinks,        ArrayList<uma_GraphConnector> uma_graphconnectors    ) {
        this.uma_diagramlinks = uma_diagramlinks;
        this.uma_graphconnectors = uma_graphconnectors;
    }


    public uma_GraphConnector getUma_graphconnector() {
        return uma_graphconnector;
    }

    public void setUma_graphconnector(uma_GraphConnector uma_graphconnector) {
        this.uma_graphconnector = uma_graphconnector;
    }
    public uma_DiagramLink getUma_diagramlink() {
        return uma_diagramlink;
    }

    public void setUma_diagramlink(uma_DiagramLink uma_diagramlink) {
        this.uma_diagramlink = uma_diagramlink;
    }
    public uma_SemanticModelBridge getUma_semanticmodelbridge() {
        return uma_semanticmodelbridge;
    }

    public void setUma_semanticmodelbridge(uma_SemanticModelBridge uma_semanticmodelbridge) {
        this.uma_semanticmodelbridge = uma_semanticmodelbridge;
    }
    public uma_SemanticModelBridge getUma_semanticmodelbridge() {
        return uma_semanticmodelbridge;
    }

    public void setUma_semanticmodelbridge(uma_SemanticModelBridge uma_semanticmodelbridge) {
        this.uma_semanticmodelbridge = uma_semanticmodelbridge;
    }
    public List<uma_DiagramLink> getUma_diagramlinks() {
        return uma_diagramlinks;
    }

    public void addUma_diagramlink(Uma_diagramlink uma_diagramlink) {
        this.uma_diagramlinks.add(uma_diagramlink);
    }
    public List<uma_GraphConnector> getUma_graphconnectors() {
        return uma_graphconnectors;
    }

    public void addUma_graphconnector(Uma_graphconnector uma_graphconnector) {
        this.uma_graphconnectors.add(uma_graphconnector);
    }
    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }

}