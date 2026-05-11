





import java.util.List;
import java.util.ArrayList;

public class flowchart_Node  {

    private String name;





    private flowchart_Flowchart flowchart_flowchart;


    public flowchart_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public flowchart_Flowchart getFlowchart_flowchart() {
        return flowchart_flowchart;
    }

    public void setFlowchart_flowchart(flowchart_Flowchart flowchart_flowchart) {
        this.flowchart_flowchart = flowchart_flowchart;
    }

}