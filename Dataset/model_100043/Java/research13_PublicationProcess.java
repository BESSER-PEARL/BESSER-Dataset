





import java.util.List;
import java.util.ArrayList;

public class research13_PublicationProcess extends Named {

    private int minTime;
    private int maxTime;





    private List<research13_Phase> research13_phases;


    public research13_PublicationProcess(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.research13_phases = new ArrayList<>();
    }

    public research13_PublicationProcess(
        int minTime,        int maxTime        ArrayList<research13_Phase> research13_phases    ) {
        this.minTime = minTime;
        this.maxTime = maxTime;
        this.research13_phases = research13_phases;
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

    public List<research13_Phase> getResearch13_phases() {
        return research13_phases;
    }

    public void addResearch13_phase(Research13_phase research13_phase) {
        this.research13_phases.add(research13_phase);
    }

}