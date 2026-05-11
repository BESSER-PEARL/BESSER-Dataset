





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Lane extends BaseElement, InteractionNode {






    private bpmn2_DocumentRoot bpmn2_documentroot;




    private List<bpmn2_Performer> bpmn2_performers;




    private List<bpmn2_FlowNode> bpmn2_flownodes;




    private bpmn2_FlowNode bpmn2_flownode;




    private List<bpmn2_BaseElement> bpmn2_baseelements;




    private bpmn2_BaseElement bpmn2_baseelement;


    public bpmn2_Lane(
    ) {
        super(
        );
        this.bpmn2_performers = new ArrayList<>();
        this.bpmn2_flownodes = new ArrayList<>();
        this.bpmn2_baseelements = new ArrayList<>();
    }

    public bpmn2_Lane(
        ArrayList<bpmn2_Performer> bpmn2_performers,        ArrayList<bpmn2_FlowNode> bpmn2_flownodes,        ArrayList<bpmn2_BaseElement> bpmn2_baseelements    ) {
        this.bpmn2_performers = bpmn2_performers;
        this.bpmn2_flownodes = bpmn2_flownodes;
        this.bpmn2_baseelements = bpmn2_baseelements;
    }


    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public List<bpmn2_Performer> getBpmn2_performers() {
        return bpmn2_performers;
    }

    public void addBpmn2_performer(Bpmn2_performer bpmn2_performer) {
        this.bpmn2_performers.add(bpmn2_performer);
    }
    public List<bpmn2_FlowNode> getBpmn2_flownodes() {
        return bpmn2_flownodes;
    }

    public void addBpmn2_flownode(Bpmn2_flownode bpmn2_flownode) {
        this.bpmn2_flownodes.add(bpmn2_flownode);
    }
    public bpmn2_FlowNode getBpmn2_flownode() {
        return bpmn2_flownode;
    }

    public void setBpmn2_flownode(bpmn2_FlowNode bpmn2_flownode) {
        this.bpmn2_flownode = bpmn2_flownode;
    }
    public List<bpmn2_BaseElement> getBpmn2_baseelements() {
        return bpmn2_baseelements;
    }

    public void addBpmn2_baseelement(Bpmn2_baseelement bpmn2_baseelement) {
        this.bpmn2_baseelements.add(bpmn2_baseelement);
    }
    public bpmn2_BaseElement getBpmn2_baseelement() {
        return bpmn2_baseelement;
    }

    public void setBpmn2_baseelement(bpmn2_BaseElement bpmn2_baseelement) {
        this.bpmn2_baseelement = bpmn2_baseelement;
    }

}