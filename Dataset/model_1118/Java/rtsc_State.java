





import java.util.List;
import java.util.ArrayList;

public class rtsc_State extends Vertex, NamedElement {

    private boolean final;
    private boolean initial;





    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private List<rtsc_Realtimestatechart> rtsc_realtimestatecharts;


    public rtsc_State(
        boolean final,        boolean initial    ) {
        super(
        );
        this.final = final;
        this.initial = initial;
        this.rtsc_realtimestatecharts = new ArrayList<>();
    }

    public rtsc_State(
        boolean final,        boolean initial        ArrayList<rtsc_Realtimestatechart> rtsc_realtimestatecharts    ) {
        this.final = final;
        this.initial = initial;
        this.rtsc_realtimestatecharts = rtsc_realtimestatecharts;
    }

    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public List<rtsc_Realtimestatechart> getRtsc_realtimestatecharts() {
        return rtsc_realtimestatecharts;
    }

    public void addRtsc_realtimestatechart(Rtsc_realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatecharts.add(rtsc_realtimestatechart);
    }

}