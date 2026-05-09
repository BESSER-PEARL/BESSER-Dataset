





import java.util.List;
import java.util.ArrayList;

public class research19_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;





    private List<research19_Phase> research19_phases;


    public research19_PublicationProcess(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.research19_phases = new ArrayList<>();
    }

    public research19_PublicationProcess(
        int minTime,        int maxTime        ArrayList<research19_Phase> research19_phases    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.research19_phases = research19_phases;
    }

    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }

    public List<research19_Phase> getResearch19_phases() {
        return research19_phases;
    }

    public void addResearch19_phase(Research19_phase research19_phase) {
        this.research19_phases.add(research19_phase);
    }

}