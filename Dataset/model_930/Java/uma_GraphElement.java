





import java.util.List;
import java.util.ArrayList;

public class uma_GraphElement extends DiagramElement {






    private List<uma_GraphConnector> uma_graphconnectors;




    private List<uma_DiagramElement> uma_diagramelements;




    private uma_Point uma_point;




    private uma_DiagramElement uma_diagramelement;




    private uma_SemanticModelBridge uma_semanticmodelbridge;




    private uma_SemanticModelBridge uma_semanticmodelbridge;




    private uma_GraphConnector uma_graphconnector;


    public uma_GraphElement(
    ) {
        super(
        );
        this.uma_graphconnectors = new ArrayList<>();
        this.uma_diagramelements = new ArrayList<>();
    }

    public uma_GraphElement(
        ArrayList<uma_GraphConnector> uma_graphconnectors,        ArrayList<uma_DiagramElement> uma_diagramelements    ) {
        this.uma_graphconnectors = uma_graphconnectors;
        this.uma_diagramelements = uma_diagramelements;
    }


    public List<uma_GraphConnector> getUma_graphconnectors() {
        return uma_graphconnectors;
    }

    public void addUma_graphconnector(Uma_graphconnector uma_graphconnector) {
        this.uma_graphconnectors.add(uma_graphconnector);
    }
    public List<uma_DiagramElement> getUma_diagramelements() {
        return uma_diagramelements;
    }

    public void addUma_diagramelement(Uma_diagramelement uma_diagramelement) {
        this.uma_diagramelements.add(uma_diagramelement);
    }
    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }
    public uma_DiagramElement getUma_diagramelement() {
        return uma_diagramelement;
    }

    public void setUma_diagramelement(uma_DiagramElement uma_diagramelement) {
        this.uma_diagramelement = uma_diagramelement;
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
    public uma_GraphConnector getUma_graphconnector() {
        return uma_graphconnector;
    }

    public void setUma_graphconnector(uma_GraphConnector uma_graphconnector) {
        this.uma_graphconnector = uma_graphconnector;
    }

}