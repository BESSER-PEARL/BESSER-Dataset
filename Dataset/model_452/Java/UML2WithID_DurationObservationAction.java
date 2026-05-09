





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DurationObservationAction extends WriteStructuralFeatureAction {






    private List<UML2WithID_Duration> uml2withid_durations;


    public UML2WithID_DurationObservationAction(
    ) {
        super(
        );
        this.uml2withid_durations = new ArrayList<>();
    }

    public UML2WithID_DurationObservationAction(
        ArrayList<UML2WithID_Duration> uml2withid_durations    ) {
        this.uml2withid_durations = uml2withid_durations;
    }


    public List<UML2WithID_Duration> getUml2withid_durations() {
        return uml2withid_durations;
    }

    public void addUml2withid_duration(Uml2withid_duration uml2withid_duration) {
        this.uml2withid_durations.add(uml2withid_duration);
    }

}