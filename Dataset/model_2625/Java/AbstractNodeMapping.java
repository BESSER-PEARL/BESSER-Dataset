





import java.util.List;
import java.util.ArrayList;

public class AbstractNodeMapping  {






    private diagram_description_OrderedTreeLayout diagram_description_orderedtreelayout;




    private diagram_description_EdgeMapping diagram_description_edgemapping;




    private diagram_tool_ContainerCreationDescription diagram_tool_containercreationdescription;




    private diagram_tool_NodeCreationDescription diagram_tool_nodecreationdescription;


    public AbstractNodeMapping(
    ) {
    }



    public diagram_description_OrderedTreeLayout getDiagram_description_orderedtreelayout() {
        return diagram_description_orderedtreelayout;
    }

    public void setDiagram_description_orderedtreelayout(diagram_description_OrderedTreeLayout diagram_description_orderedtreelayout) {
        this.diagram_description_orderedtreelayout = diagram_description_orderedtreelayout;
    }
    public diagram_description_EdgeMapping getDiagram_description_edgemapping() {
        return diagram_description_edgemapping;
    }

    public void setDiagram_description_edgemapping(diagram_description_EdgeMapping diagram_description_edgemapping) {
        this.diagram_description_edgemapping = diagram_description_edgemapping;
    }
    public diagram_tool_ContainerCreationDescription getDiagram_tool_containercreationdescription() {
        return diagram_tool_containercreationdescription;
    }

    public void setDiagram_tool_containercreationdescription(diagram_tool_ContainerCreationDescription diagram_tool_containercreationdescription) {
        this.diagram_tool_containercreationdescription = diagram_tool_containercreationdescription;
    }
    public diagram_tool_NodeCreationDescription getDiagram_tool_nodecreationdescription() {
        return diagram_tool_nodecreationdescription;
    }

    public void setDiagram_tool_nodecreationdescription(diagram_tool_NodeCreationDescription diagram_tool_nodecreationdescription) {
        this.diagram_tool_nodecreationdescription = diagram_tool_nodecreationdescription;
    }

}