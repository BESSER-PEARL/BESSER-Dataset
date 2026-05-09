





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_MarkovSchedulingState  {

    private String name;
    private String firings;





    private List<MarkovSchedulingTransition> markovschedulingtransitions;




    private List<MarkovSchedulingTransition> markovschedulingtransitions;




    private scheduling_analysis_Actor scheduling_analysis_actor;


    public analysis_scheduling_MarkovSchedulingState(
        String name,        String firings    ) {
        this.name = name;
        this.firings = firings;
        this.markovschedulingtransitions = new ArrayList<>();
        this.markovschedulingtransitions = new ArrayList<>();
    }

    public analysis_scheduling_MarkovSchedulingState(
        String name,        String firings        ArrayList<MarkovSchedulingTransition> markovschedulingtransitions,        ArrayList<MarkovSchedulingTransition> markovschedulingtransitions    ) {
        this.name = name;
        this.firings = firings;
        this.markovschedulingtransitions = markovschedulingtransitions;
        this.markovschedulingtransitions = markovschedulingtransitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFirings() {
        return firings;
    }

    public void setFirings(String firings) {
        this.firings = firings;
    }

    public List<MarkovSchedulingTransition> getMarkovschedulingtransitions() {
        return markovschedulingtransitions;
    }

    public void addMarkovschedulingtransition(Markovschedulingtransition markovschedulingtransition) {
        this.markovschedulingtransitions.add(markovschedulingtransition);
    }
    public List<MarkovSchedulingTransition> getMarkovschedulingtransitions() {
        return markovschedulingtransitions;
    }

    public void addMarkovschedulingtransition(Markovschedulingtransition markovschedulingtransition) {
        this.markovschedulingtransitions.add(markovschedulingtransition);
    }
    public scheduling_analysis_Actor getScheduling_analysis_actor() {
        return scheduling_analysis_actor;
    }

    public void setScheduling_analysis_actor(scheduling_analysis_Actor scheduling_analysis_actor) {
        this.scheduling_analysis_actor = scheduling_analysis_actor;
    }

}