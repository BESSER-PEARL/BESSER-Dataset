





import java.util.List;
import java.util.ArrayList;

public class research2_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private List<research2_Phase> research2_phases;


    public research2_PublicationProcess(
        int maxTime,        int minTime    ) {
        super(
        );
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.research2_phases = new ArrayList<>();
    }

    public research2_PublicationProcess(
        int maxTime,        int minTime        ArrayList<research2_Phase> research2_phases    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.research2_phases = research2_phases;
    }

    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }
    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }

    public List<research2_Phase> getResearch2_phases() {
        return research2_phases;
    }

    public void addResearch2_phase(Research2_phase research2_phase) {
        this.research2_phases.add(research2_phase);
    }

}