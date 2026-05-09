





import java.util.List;
import java.util.ArrayList;

public class statemachines_Operation extends NamedElement {






    private statemachines_CallEventOccurrence statemachines_calleventoccurrence;




    private statemachines_CustomSystem statemachines_customsystem;


    public statemachines_Operation(
    ) {
        super(
        );
    }



    public statemachines_CallEventOccurrence getStatemachines_calleventoccurrence() {
        return statemachines_calleventoccurrence;
    }

    public void setStatemachines_calleventoccurrence(statemachines_CallEventOccurrence statemachines_calleventoccurrence) {
        this.statemachines_calleventoccurrence = statemachines_calleventoccurrence;
    }
    public statemachines_CustomSystem getStatemachines_customsystem() {
        return statemachines_customsystem;
    }

    public void setStatemachines_customsystem(statemachines_CustomSystem statemachines_customsystem) {
        this.statemachines_customsystem = statemachines_customsystem;
    }

}