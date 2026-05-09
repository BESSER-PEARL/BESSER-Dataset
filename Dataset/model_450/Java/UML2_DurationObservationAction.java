





import java.util.List;
import java.util.ArrayList;

public class UML2_DurationObservationAction extends WriteStructuralFeatureAction {






    private List<UML2_Duration> uml2_durations;


    public UML2_DurationObservationAction(
    ) {
        super(
        );
        this.uml2_durations = new ArrayList<>();
    }

    public UML2_DurationObservationAction(
        ArrayList<UML2_Duration> uml2_durations    ) {
        this.uml2_durations = uml2_durations;
    }


    public List<UML2_Duration> getUml2_durations() {
        return uml2_durations;
    }

    public void addUml2_duration(Uml2_duration uml2_duration) {
        this.uml2_durations.add(uml2_duration);
    }

}