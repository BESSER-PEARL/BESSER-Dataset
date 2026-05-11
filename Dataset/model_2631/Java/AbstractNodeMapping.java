





import java.util.List;
import java.util.ArrayList;

public class AbstractNodeMapping  {






    private diagram_description_EdgeMapping diagram_description_edgemapping;




    private diagram_description_OrderedTreeLayout diagram_description_orderedtreelayout;


    public AbstractNodeMapping(
    ) {
    }



    public diagram_description_EdgeMapping getDiagram_description_edgemapping() {
        return diagram_description_edgemapping;
    }

    public void setDiagram_description_edgemapping(diagram_description_EdgeMapping diagram_description_edgemapping) {
        this.diagram_description_edgemapping = diagram_description_edgemapping;
    }
    public diagram_description_OrderedTreeLayout getDiagram_description_orderedtreelayout() {
        return diagram_description_orderedtreelayout;
    }

    public void setDiagram_description_orderedtreelayout(diagram_description_OrderedTreeLayout diagram_description_orderedtreelayout) {
        this.diagram_description_orderedtreelayout = diagram_description_orderedtreelayout;
    }

}