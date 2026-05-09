





import java.util.List;
import java.util.ArrayList;

public class analysis_profiling_IntraActionCommunicationData  {






    private profiling_analysis_StatisticalData profiling_analysis_statisticaldata;




    private List<ActionToStatisticalDataMap> actiontostatisticaldatamaps;




    private profiling_analysis_StatisticalData profiling_analysis_statisticaldata;


    public analysis_profiling_IntraActionCommunicationData(
    ) {
        this.actiontostatisticaldatamaps = new ArrayList<>();
    }

    public analysis_profiling_IntraActionCommunicationData(
        ArrayList<ActionToStatisticalDataMap> actiontostatisticaldatamaps    ) {
        this.actiontostatisticaldatamaps = actiontostatisticaldatamaps;
    }


    public profiling_analysis_StatisticalData getProfiling_analysis_statisticaldata() {
        return profiling_analysis_statisticaldata;
    }

    public void setProfiling_analysis_statisticaldata(profiling_analysis_StatisticalData profiling_analysis_statisticaldata) {
        this.profiling_analysis_statisticaldata = profiling_analysis_statisticaldata;
    }
    public List<ActionToStatisticalDataMap> getActiontostatisticaldatamaps() {
        return actiontostatisticaldatamaps;
    }

    public void addActiontostatisticaldatamap(Actiontostatisticaldatamap actiontostatisticaldatamap) {
        this.actiontostatisticaldatamaps.add(actiontostatisticaldatamap);
    }
    public profiling_analysis_StatisticalData getProfiling_analysis_statisticaldata() {
        return profiling_analysis_statisticaldata;
    }

    public void setProfiling_analysis_statisticaldata(profiling_analysis_StatisticalData profiling_analysis_statisticaldata) {
        this.profiling_analysis_statisticaldata = profiling_analysis_statisticaldata;
    }

}