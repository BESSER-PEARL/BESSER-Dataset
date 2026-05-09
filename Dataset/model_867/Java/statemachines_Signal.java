





import java.util.List;
import java.util.ArrayList;

public class statemachines_Signal extends NamedElement {






    private statemachines_SignalEventOccurrence statemachines_signaleventoccurrence;




    private statemachines_CustomSystem statemachines_customsystem;


    public statemachines_Signal(
    ) {
        super(
        );
    }



    public statemachines_SignalEventOccurrence getStatemachines_signaleventoccurrence() {
        return statemachines_signaleventoccurrence;
    }

    public void setStatemachines_signaleventoccurrence(statemachines_SignalEventOccurrence statemachines_signaleventoccurrence) {
        this.statemachines_signaleventoccurrence = statemachines_signaleventoccurrence;
    }
    public statemachines_CustomSystem getStatemachines_customsystem() {
        return statemachines_customsystem;
    }

    public void setStatemachines_customsystem(statemachines_CustomSystem statemachines_customsystem) {
        this.statemachines_customsystem = statemachines_customsystem;
    }

}