





import java.util.List;
import java.util.ArrayList;

public class sam_FlowGroup extends ENamedElement {

    private String globalComment;





    private sam_Flow sam_flow;




    private List<sam_Flow> sam_flows;


    public sam_FlowGroup(
        String globalComment    ) {
        super(
        );
        this.globalComment = globalComment;
        this.sam_flows = new ArrayList<>();
    }

    public sam_FlowGroup(
        String globalComment        ArrayList<sam_Flow> sam_flows    ) {
        this.globalComment = globalComment;
        this.sam_flows = sam_flows;
    }

    public String getGlobalcomment() {
        return globalComment;
    }

    public void setGlobalcomment(String globalComment) {
        this.globalComment = globalComment;
    }

    public sam_Flow getSam_flow() {
        return sam_flow;
    }

    public void setSam_flow(sam_Flow sam_flow) {
        this.sam_flow = sam_flow;
    }
    public List<sam_Flow> getSam_flows() {
        return sam_flows;
    }

    public void addSam_flow(Sam_flow sam_flow) {
        this.sam_flows.add(sam_flow);
    }

}