





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_ScheduledImpactAnalysisData  {






    private List<DoubleToDoubleMap> doubletodoublemaps;




    private List<DoubleToDoubleMap> doubletodoublemaps;




    private bottlenecks_analysis_ActorClass bottlenecks_analysis_actorclass;




    private List<bottlenecks_analysis_Action> bottlenecks_analysis_actions;


    public analysis_bottlenecks_ScheduledImpactAnalysisData(
    ) {
        this.doubletodoublemaps = new ArrayList<>();
        this.doubletodoublemaps = new ArrayList<>();
        this.bottlenecks_analysis_actions = new ArrayList<>();
    }

    public analysis_bottlenecks_ScheduledImpactAnalysisData(
        ArrayList<DoubleToDoubleMap> doubletodoublemaps,        ArrayList<DoubleToDoubleMap> doubletodoublemaps,        ArrayList<bottlenecks_analysis_Action> bottlenecks_analysis_actions    ) {
        this.doubletodoublemaps = doubletodoublemaps;
        this.doubletodoublemaps = doubletodoublemaps;
        this.bottlenecks_analysis_actions = bottlenecks_analysis_actions;
    }


    public List<DoubleToDoubleMap> getDoubletodoublemaps() {
        return doubletodoublemaps;
    }

    public void addDoubletodoublemap(Doubletodoublemap doubletodoublemap) {
        this.doubletodoublemaps.add(doubletodoublemap);
    }
    public List<DoubleToDoubleMap> getDoubletodoublemaps() {
        return doubletodoublemaps;
    }

    public void addDoubletodoublemap(Doubletodoublemap doubletodoublemap) {
        this.doubletodoublemaps.add(doubletodoublemap);
    }
    public bottlenecks_analysis_ActorClass getBottlenecks_analysis_actorclass() {
        return bottlenecks_analysis_actorclass;
    }

    public void setBottlenecks_analysis_actorclass(bottlenecks_analysis_ActorClass bottlenecks_analysis_actorclass) {
        this.bottlenecks_analysis_actorclass = bottlenecks_analysis_actorclass;
    }
    public List<bottlenecks_analysis_Action> getBottlenecks_analysis_actions() {
        return bottlenecks_analysis_actions;
    }

    public void addBottlenecks_analysis_action(Bottlenecks_analysis_action bottlenecks_analysis_action) {
        this.bottlenecks_analysis_actions.add(bottlenecks_analysis_action);
    }

}