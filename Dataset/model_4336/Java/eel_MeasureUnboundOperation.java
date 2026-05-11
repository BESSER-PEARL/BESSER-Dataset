





import java.util.List;
import java.util.ArrayList;

public class eel_MeasureUnboundOperation extends TypedMeasure {






    private List<eel_Measure> eel_measures;


    public eel_MeasureUnboundOperation(
    ) {
        super(
        );
        this.eel_measures = new ArrayList<>();
    }

    public eel_MeasureUnboundOperation(
        ArrayList<eel_Measure> eel_measures    ) {
        this.eel_measures = eel_measures;
    }


    public List<eel_Measure> getEel_measures() {
        return eel_measures;
    }

    public void addEel_measure(Eel_measure eel_measure) {
        this.eel_measures.add(eel_measure);
    }

}