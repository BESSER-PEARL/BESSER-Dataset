





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_SymbolicParameter  {

    private String name;





    private EventAutomatonModel_Automaton eventautomatonmodel_automaton;


    public EventAutomatonModel_SymbolicParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EventAutomatonModel_Automaton getEventautomatonmodel_automaton() {
        return eventautomatonmodel_automaton;
    }

    public void setEventautomatonmodel_automaton(EventAutomatonModel_Automaton eventautomatonmodel_automaton) {
        this.eventautomatonmodel_automaton = eventautomatonmodel_automaton;
    }

}