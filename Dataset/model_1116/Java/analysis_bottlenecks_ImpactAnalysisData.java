





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_ImpactAnalysisData  {






    private List<bottlenecks_analysis_Action> bottlenecks_analysis_actions;


    public analysis_bottlenecks_ImpactAnalysisData(
    ) {
        this.bottlenecks_analysis_actions = new ArrayList<>();
    }

    public analysis_bottlenecks_ImpactAnalysisData(
        ArrayList<bottlenecks_analysis_Action> bottlenecks_analysis_actions    ) {
        this.bottlenecks_analysis_actions = bottlenecks_analysis_actions;
    }


    public List<bottlenecks_analysis_Action> getBottlenecks_analysis_actions() {
        return bottlenecks_analysis_actions;
    }

    public void addBottlenecks_analysis_action(Bottlenecks_analysis_action bottlenecks_analysis_action) {
        this.bottlenecks_analysis_actions.add(bottlenecks_analysis_action);
    }

}