





import java.util.List;
import java.util.ArrayList;

public class RepresentationGraph_ContainerElement extends NodeElement {






    private List<RepresentationGraph_NodeElement> representationgraph_nodeelements;


    public RepresentationGraph_ContainerElement(
    ) {
        super(
        );
        this.representationgraph_nodeelements = new ArrayList<>();
    }

    public RepresentationGraph_ContainerElement(
        ArrayList<RepresentationGraph_NodeElement> representationgraph_nodeelements    ) {
        this.representationgraph_nodeelements = representationgraph_nodeelements;
    }


    public List<RepresentationGraph_NodeElement> getRepresentationgraph_nodeelements() {
        return representationgraph_nodeelements;
    }

    public void addRepresentationgraph_nodeelement(Representationgraph_nodeelement representationgraph_nodeelement) {
        this.representationgraph_nodeelements.add(representationgraph_nodeelement);
    }

}