





import java.util.List;
import java.util.ArrayList;

public class analysis_postprocessing_ActionStatisticsReport extends PostProcessingData {






    private List<ActionToLongMap> actiontolongmaps;


    public analysis_postprocessing_ActionStatisticsReport(
    ) {
        super(
        );
        this.actiontolongmaps = new ArrayList<>();
    }

    public analysis_postprocessing_ActionStatisticsReport(
        ArrayList<ActionToLongMap> actiontolongmaps    ) {
        this.actiontolongmaps = actiontolongmaps;
    }


    public List<ActionToLongMap> getActiontolongmaps() {
        return actiontolongmaps;
    }

    public void addActiontolongmap(Actiontolongmap actiontolongmap) {
        this.actiontolongmaps.add(actiontolongmap);
    }

}