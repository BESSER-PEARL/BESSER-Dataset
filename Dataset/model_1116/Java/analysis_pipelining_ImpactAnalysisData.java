





import java.util.List;
import java.util.ArrayList;

public class analysis_pipelining_ImpactAnalysisData  {

    private float cpReduction;





    private BottlenecksReport bottlenecksreport;




    private List<pipelining_analysis_Action> pipelining_analysis_actions;


    public analysis_pipelining_ImpactAnalysisData(
        float cpReduction    ) {
        this.cpReduction = cpReduction;
        this.pipelining_analysis_actions = new ArrayList<>();
    }

    public analysis_pipelining_ImpactAnalysisData(
        float cpReduction        ArrayList<pipelining_analysis_Action> pipelining_analysis_actions    ) {
        this.cpReduction = cpReduction;
        this.pipelining_analysis_actions = pipelining_analysis_actions;
    }

    public float getCpreduction() {
        return cpReduction;
    }

    public void setCpreduction(float cpReduction) {
        this.cpReduction = cpReduction;
    }

    public BottlenecksReport getBottlenecksreport() {
        return bottlenecksreport;
    }

    public void setBottlenecksreport(BottlenecksReport bottlenecksreport) {
        this.bottlenecksreport = bottlenecksreport;
    }
    public List<pipelining_analysis_Action> getPipelining_analysis_actions() {
        return pipelining_analysis_actions;
    }

    public void addPipelining_analysis_action(Pipelining_analysis_action pipelining_analysis_action) {
        this.pipelining_analysis_actions.add(pipelining_analysis_action);
    }

}