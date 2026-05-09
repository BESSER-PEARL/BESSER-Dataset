





import java.util.List;
import java.util.ArrayList;

public class rtsc_Realtimestatechart extends Behavior, NamedElement {

    private int rounds;





    private List<rtsc_Clock> rtsc_clocks;




    private rtsc_Clock rtsc_clock;




    private rtsc_Variable rtsc_variable;




    private List<rtsc_Variable> rtsc_variables;




    private rtsc_System rtsc_system;


    public rtsc_Realtimestatechart(
        int rounds    ) {
        super(
        );
        this.rounds = rounds;
        this.rtsc_clocks = new ArrayList<>();
        this.rtsc_variables = new ArrayList<>();
    }

    public rtsc_Realtimestatechart(
        int rounds        ArrayList<rtsc_Clock> rtsc_clocks,        ArrayList<rtsc_Variable> rtsc_variables    ) {
        this.rounds = rounds;
        this.rtsc_clocks = rtsc_clocks;
        this.rtsc_variables = rtsc_variables;
    }

    public int getRounds() {
        return rounds;
    }

    public void setRounds(int rounds) {
        this.rounds = rounds;
    }

    public List<rtsc_Clock> getRtsc_clocks() {
        return rtsc_clocks;
    }

    public void addRtsc_clock(Rtsc_clock rtsc_clock) {
        this.rtsc_clocks.add(rtsc_clock);
    }
    public rtsc_Clock getRtsc_clock() {
        return rtsc_clock;
    }

    public void setRtsc_clock(rtsc_Clock rtsc_clock) {
        this.rtsc_clock = rtsc_clock;
    }
    public rtsc_Variable getRtsc_variable() {
        return rtsc_variable;
    }

    public void setRtsc_variable(rtsc_Variable rtsc_variable) {
        this.rtsc_variable = rtsc_variable;
    }
    public List<rtsc_Variable> getRtsc_variables() {
        return rtsc_variables;
    }

    public void addRtsc_variable(Rtsc_variable rtsc_variable) {
        this.rtsc_variables.add(rtsc_variable);
    }
    public rtsc_System getRtsc_system() {
        return rtsc_system;
    }

    public void setRtsc_system(rtsc_System rtsc_system) {
        this.rtsc_system = rtsc_system;
    }

}