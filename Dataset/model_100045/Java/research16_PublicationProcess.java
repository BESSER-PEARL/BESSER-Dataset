





import java.util.List;
import java.util.ArrayList;

public class research16_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private List<research16_Phase> research16_phases;


    public research16_PublicationProcess(
        int maxTime,        int minTime    ) {
        super(
        );
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.research16_phases = new ArrayList<>();
    }

    public research16_PublicationProcess(
        int maxTime,        int minTime        ArrayList<research16_Phase> research16_phases    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.research16_phases = research16_phases;
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

    public List<research16_Phase> getResearch16_phases() {
        return research16_phases;
    }

    public void addResearch16_phase(Research16_phase research16_phase) {
        this.research16_phases.add(research16_phase);
    }

}