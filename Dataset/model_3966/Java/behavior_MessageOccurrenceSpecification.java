





import java.util.List;
import java.util.ArrayList;

public class behavior_MessageOccurrenceSpecification extends OccurrenceSpecification, MessageEnd {






    private behavior_Event behavior_event;


    public behavior_MessageOccurrenceSpecification(
    ) {
        super(
        );
    }



    public behavior_Event getBehavior_event() {
        return behavior_event;
    }

    public void setBehavior_event(behavior_Event behavior_event) {
        this.behavior_event = behavior_event;
    }

}