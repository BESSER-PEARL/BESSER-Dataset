





import java.util.List;
import java.util.ArrayList;

public class smartadapters4MODERATES_adaptations_UnsetCompositeState extends UnsetAdaptation {






    private adaptations_smartadapters4MODERATES_State adaptations_smartadapters4moderates_state;




    private adaptations_smartadapters4MODERATES_CompositeState adaptations_smartadapters4moderates_compositestate;




    private List<adaptations_smartadapters4MODERATES_State> adaptations_smartadapters4moderates_states;


    public smartadapters4MODERATES_adaptations_UnsetCompositeState(
    ) {
        super(
        );
        this.adaptations_smartadapters4moderates_states = new ArrayList<>();
    }

    public smartadapters4MODERATES_adaptations_UnsetCompositeState(
        ArrayList<adaptations_smartadapters4MODERATES_State> adaptations_smartadapters4moderates_states    ) {
        this.adaptations_smartadapters4moderates_states = adaptations_smartadapters4moderates_states;
    }


    public adaptations_smartadapters4MODERATES_State getAdaptations_smartadapters4moderates_state() {
        return adaptations_smartadapters4moderates_state;
    }

    public void setAdaptations_smartadapters4moderates_state(adaptations_smartadapters4MODERATES_State adaptations_smartadapters4moderates_state) {
        this.adaptations_smartadapters4moderates_state = adaptations_smartadapters4moderates_state;
    }
    public adaptations_smartadapters4MODERATES_CompositeState getAdaptations_smartadapters4moderates_compositestate() {
        return adaptations_smartadapters4moderates_compositestate;
    }

    public void setAdaptations_smartadapters4moderates_compositestate(adaptations_smartadapters4MODERATES_CompositeState adaptations_smartadapters4moderates_compositestate) {
        this.adaptations_smartadapters4moderates_compositestate = adaptations_smartadapters4moderates_compositestate;
    }
    public List<adaptations_smartadapters4MODERATES_State> getAdaptations_smartadapters4moderates_states() {
        return adaptations_smartadapters4moderates_states;
    }

    public void addAdaptations_smartadapters4moderates_state(Adaptations_smartadapters4moderates_state adaptations_smartadapters4moderates_state) {
        this.adaptations_smartadapters4moderates_states.add(adaptations_smartadapters4moderates_state);
    }

}