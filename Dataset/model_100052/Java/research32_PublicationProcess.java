





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationProcess extends Named {

    private int maxTime;
    private int minTime;





    private List<research32_Phase> research32_phases;


    public research32_PublicationProcess(
        int maxTime,        int minTime    ) {
        super(
        );
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.research32_phases = new ArrayList<>();
    }

    public research32_PublicationProcess(
        int maxTime,        int minTime        ArrayList<research32_Phase> research32_phases    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.research32_phases = research32_phases;
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

    public List<research32_Phase> getResearch32_phases() {
        return research32_phases;
    }

    public void addResearch32_phase(Research32_phase research32_phase) {
        this.research32_phases.add(research32_phase);
    }

}