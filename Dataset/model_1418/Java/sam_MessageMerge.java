





import java.util.List;
import java.util.ArrayList;

public class sam_MessageMerge extends MergeGate {






    private List<sam_OutMessagePort> sam_outmessageports;




    private sam_InMessagePort sam_inmessageport;




    private List<sam_InMessagePort> sam_inmessageports;




    private sam_OutMessagePort sam_outmessageport;


    public sam_MessageMerge(
    ) {
        super(
        );
        this.sam_outmessageports = new ArrayList<>();
        this.sam_inmessageports = new ArrayList<>();
    }

    public sam_MessageMerge(
        ArrayList<sam_OutMessagePort> sam_outmessageports,        ArrayList<sam_InMessagePort> sam_inmessageports    ) {
        this.sam_outmessageports = sam_outmessageports;
        this.sam_inmessageports = sam_inmessageports;
    }


    public List<sam_OutMessagePort> getSam_outmessageports() {
        return sam_outmessageports;
    }

    public void addSam_outmessageport(Sam_outmessageport sam_outmessageport) {
        this.sam_outmessageports.add(sam_outmessageport);
    }
    public sam_InMessagePort getSam_inmessageport() {
        return sam_inmessageport;
    }

    public void setSam_inmessageport(sam_InMessagePort sam_inmessageport) {
        this.sam_inmessageport = sam_inmessageport;
    }
    public List<sam_InMessagePort> getSam_inmessageports() {
        return sam_inmessageports;
    }

    public void addSam_inmessageport(Sam_inmessageport sam_inmessageport) {
        this.sam_inmessageports.add(sam_inmessageport);
    }
    public sam_OutMessagePort getSam_outmessageport() {
        return sam_outmessageport;
    }

    public void setSam_outmessageport(sam_OutMessagePort sam_outmessageport) {
        this.sam_outmessageport = sam_outmessageport;
    }

}