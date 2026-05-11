





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DNodeListElement extends AbstractDNode {






    private NodeStyle nodestyle;




    private description_NodeMapping description_nodemapping;




    private List<description_NodeMapping> description_nodemappings;




    private diagram_viewpoint_Style diagram_viewpoint_style;


    public viewpoint_diagram_DNodeListElement(
    ) {
        super(
        );
        this.description_nodemappings = new ArrayList<>();
    }

    public viewpoint_diagram_DNodeListElement(
        ArrayList<description_NodeMapping> description_nodemappings    ) {
        this.description_nodemappings = description_nodemappings;
    }


    public NodeStyle getNodestyle() {
        return nodestyle;
    }

    public void setNodestyle(NodeStyle nodestyle) {
        this.nodestyle = nodestyle;
    }
    public description_NodeMapping getDescription_nodemapping() {
        return description_nodemapping;
    }

    public void setDescription_nodemapping(description_NodeMapping description_nodemapping) {
        this.description_nodemapping = description_nodemapping;
    }
    public List<description_NodeMapping> getDescription_nodemappings() {
        return description_nodemappings;
    }

    public void addDescription_nodemapping(Description_nodemapping description_nodemapping) {
        this.description_nodemappings.add(description_nodemapping);
    }
    public diagram_viewpoint_Style getDiagram_viewpoint_style() {
        return diagram_viewpoint_style;
    }

    public void setDiagram_viewpoint_style(diagram_viewpoint_Style diagram_viewpoint_style) {
        this.diagram_viewpoint_style = diagram_viewpoint_style;
    }

}