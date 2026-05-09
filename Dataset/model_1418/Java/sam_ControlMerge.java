





import java.util.List;
import java.util.ArrayList;

public class sam_ControlMerge extends MergeGate {






    private List<sam_OutControlPort> sam_outcontrolports;




    private sam_OutControlPort sam_outcontrolport;


    public sam_ControlMerge(
    ) {
        super(
        );
        this.sam_outcontrolports = new ArrayList<>();
    }

    public sam_ControlMerge(
        ArrayList<sam_OutControlPort> sam_outcontrolports    ) {
        this.sam_outcontrolports = sam_outcontrolports;
    }


    public List<sam_OutControlPort> getSam_outcontrolports() {
        return sam_outcontrolports;
    }

    public void addSam_outcontrolport(Sam_outcontrolport sam_outcontrolport) {
        this.sam_outcontrolports.add(sam_outcontrolport);
    }
    public sam_OutControlPort getSam_outcontrolport() {
        return sam_outcontrolport;
    }

    public void setSam_outcontrolport(sam_OutControlPort sam_outcontrolport) {
        this.sam_outcontrolport = sam_outcontrolport;
    }

}