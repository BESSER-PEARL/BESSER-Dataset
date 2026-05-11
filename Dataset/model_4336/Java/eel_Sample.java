





import java.util.List;
import java.util.ArrayList;

public class eel_Sample  {






    private eel_Sampling eel_sampling;




    private List<eel_Measure> eel_measures;


    public eel_Sample(
    ) {
        this.eel_measures = new ArrayList<>();
    }

    public eel_Sample(
        ArrayList<eel_Measure> eel_measures    ) {
        this.eel_measures = eel_measures;
    }


    public eel_Sampling getEel_sampling() {
        return eel_sampling;
    }

    public void setEel_sampling(eel_Sampling eel_sampling) {
        this.eel_sampling = eel_sampling;
    }
    public List<eel_Measure> getEel_measures() {
        return eel_measures;
    }

    public void addEel_measure(Eel_measure eel_measure) {
        this.eel_measures.add(eel_measure);
    }

}