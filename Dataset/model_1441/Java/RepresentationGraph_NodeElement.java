





import java.util.List;
import java.util.ArrayList;

public class RepresentationGraph_NodeElement extends GraphicElement {

    private String label;





    private List<RepresentationGraph_NodeElement> representationgraph_nodeelements;




    private RepresentationGraph_EdgeElement representationgraph_edgeelement;




    private RepresentationGraph_EdgeElement representationgraph_edgeelement;




    private RepresentationGraph_ContainerElement representationgraph_containerelement;


    public RepresentationGraph_NodeElement(
        String label    ) {
        super(
        );
        this.label = label;
        this.representationgraph_nodeelements = new ArrayList<>();
    }

    public RepresentationGraph_NodeElement(
        String label        ArrayList<RepresentationGraph_NodeElement> representationgraph_nodeelements    ) {
        this.label = label;
        this.representationgraph_nodeelements = representationgraph_nodeelements;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<RepresentationGraph_NodeElement> getRepresentationgraph_nodeelements() {
        return representationgraph_nodeelements;
    }

    public void addRepresentationgraph_nodeelement(Representationgraph_nodeelement representationgraph_nodeelement) {
        this.representationgraph_nodeelements.add(representationgraph_nodeelement);
    }
    public RepresentationGraph_EdgeElement getRepresentationgraph_edgeelement() {
        return representationgraph_edgeelement;
    }

    public void setRepresentationgraph_edgeelement(RepresentationGraph_EdgeElement representationgraph_edgeelement) {
        this.representationgraph_edgeelement = representationgraph_edgeelement;
    }
    public RepresentationGraph_EdgeElement getRepresentationgraph_edgeelement() {
        return representationgraph_edgeelement;
    }

    public void setRepresentationgraph_edgeelement(RepresentationGraph_EdgeElement representationgraph_edgeelement) {
        this.representationgraph_edgeelement = representationgraph_edgeelement;
    }
    public RepresentationGraph_ContainerElement getRepresentationgraph_containerelement() {
        return representationgraph_containerelement;
    }

    public void setRepresentationgraph_containerelement(RepresentationGraph_ContainerElement representationgraph_containerelement) {
        this.representationgraph_containerelement = representationgraph_containerelement;
    }

}