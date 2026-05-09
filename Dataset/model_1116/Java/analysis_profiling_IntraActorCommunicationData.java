





import java.util.List;
import java.util.ArrayList;

public class analysis_profiling_IntraActorCommunicationData  {






    private List<IntraActionCommunicationData> intraactioncommunicationdatas;




    private profiling_analysis_StatisticalData profiling_analysis_statisticaldata;




    private List<ActorToStatisticalDataMap> actortostatisticaldatamaps;




    private profiling_analysis_StatisticalData profiling_analysis_statisticaldata;


    public analysis_profiling_IntraActorCommunicationData(
    ) {
        this.intraactioncommunicationdatas = new ArrayList<>();
        this.actortostatisticaldatamaps = new ArrayList<>();
    }

    public analysis_profiling_IntraActorCommunicationData(
        ArrayList<IntraActionCommunicationData> intraactioncommunicationdatas,        ArrayList<ActorToStatisticalDataMap> actortostatisticaldatamaps    ) {
        this.intraactioncommunicationdatas = intraactioncommunicationdatas;
        this.actortostatisticaldatamaps = actortostatisticaldatamaps;
    }


    public List<IntraActionCommunicationData> getIntraactioncommunicationdatas() {
        return intraactioncommunicationdatas;
    }

    public void addIntraactioncommunicationdata(Intraactioncommunicationdata intraactioncommunicationdata) {
        this.intraactioncommunicationdatas.add(intraactioncommunicationdata);
    }
    public profiling_analysis_StatisticalData getProfiling_analysis_statisticaldata() {
        return profiling_analysis_statisticaldata;
    }

    public void setProfiling_analysis_statisticaldata(profiling_analysis_StatisticalData profiling_analysis_statisticaldata) {
        this.profiling_analysis_statisticaldata = profiling_analysis_statisticaldata;
    }
    public List<ActorToStatisticalDataMap> getActortostatisticaldatamaps() {
        return actortostatisticaldatamaps;
    }

    public void addActortostatisticaldatamap(Actortostatisticaldatamap actortostatisticaldatamap) {
        this.actortostatisticaldatamaps.add(actortostatisticaldatamap);
    }
    public profiling_analysis_StatisticalData getProfiling_analysis_statisticaldata() {
        return profiling_analysis_statisticaldata;
    }

    public void setProfiling_analysis_statisticaldata(profiling_analysis_StatisticalData profiling_analysis_statisticaldata) {
        this.profiling_analysis_statisticaldata = profiling_analysis_statisticaldata;
    }

}