





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_State  {

    private String acceptor;
    private int id;





    private EventAutomatonModel_Token eventautomatonmodel_token;




    private EventAutomatonModel_Automaton eventautomatonmodel_automaton;




    private EventAutomatonModel_AbstractTransition eventautomatonmodel_abstracttransition;




    private List<EventAutomatonModel_AbstractTransition> eventautomatonmodel_abstracttransitions;




    private EventAutomatonModel_Automaton eventautomatonmodel_automaton;




    private List<EventAutomatonModel_AbstractTransition> eventautomatonmodel_abstracttransitions;




    private EventAutomatonModel_AbstractTransition eventautomatonmodel_abstracttransition;




    private List<EventAutomatonModel_Token> eventautomatonmodel_tokens;




    private EventAutomatonModel_Automaton eventautomatonmodel_automaton;


    public EventAutomatonModel_State(
        String acceptor,        int id    ) {
        this.acceptor = acceptor;
        this.id = id;
        this.eventautomatonmodel_abstracttransitions = new ArrayList<>();
        this.eventautomatonmodel_abstracttransitions = new ArrayList<>();
        this.eventautomatonmodel_tokens = new ArrayList<>();
    }

    public EventAutomatonModel_State(
        String acceptor,        int id        ArrayList<EventAutomatonModel_AbstractTransition> eventautomatonmodel_abstracttransitions,        ArrayList<EventAutomatonModel_AbstractTransition> eventautomatonmodel_abstracttransitions,        ArrayList<EventAutomatonModel_Token> eventautomatonmodel_tokens    ) {
        this.acceptor = acceptor;
        this.id = id;
        this.eventautomatonmodel_abstracttransitions = eventautomatonmodel_abstracttransitions;
        this.eventautomatonmodel_abstracttransitions = eventautomatonmodel_abstracttransitions;
        this.eventautomatonmodel_tokens = eventautomatonmodel_tokens;
    }

    public String getAcceptor() {
        return acceptor;
    }

    public void setAcceptor(String acceptor) {
        this.acceptor = acceptor;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public EventAutomatonModel_Token getEventautomatonmodel_token() {
        return eventautomatonmodel_token;
    }

    public void setEventautomatonmodel_token(EventAutomatonModel_Token eventautomatonmodel_token) {
        this.eventautomatonmodel_token = eventautomatonmodel_token;
    }
    public EventAutomatonModel_Automaton getEventautomatonmodel_automaton() {
        return eventautomatonmodel_automaton;
    }

    public void setEventautomatonmodel_automaton(EventAutomatonModel_Automaton eventautomatonmodel_automaton) {
        this.eventautomatonmodel_automaton = eventautomatonmodel_automaton;
    }
    public EventAutomatonModel_AbstractTransition getEventautomatonmodel_abstracttransition() {
        return eventautomatonmodel_abstracttransition;
    }

    public void setEventautomatonmodel_abstracttransition(EventAutomatonModel_AbstractTransition eventautomatonmodel_abstracttransition) {
        this.eventautomatonmodel_abstracttransition = eventautomatonmodel_abstracttransition;
    }
    public List<EventAutomatonModel_AbstractTransition> getEventautomatonmodel_abstracttransitions() {
        return eventautomatonmodel_abstracttransitions;
    }

    public void addEventautomatonmodel_abstracttransition(Eventautomatonmodel_abstracttransition eventautomatonmodel_abstracttransition) {
        this.eventautomatonmodel_abstracttransitions.add(eventautomatonmodel_abstracttransition);
    }
    public EventAutomatonModel_Automaton getEventautomatonmodel_automaton() {
        return eventautomatonmodel_automaton;
    }

    public void setEventautomatonmodel_automaton(EventAutomatonModel_Automaton eventautomatonmodel_automaton) {
        this.eventautomatonmodel_automaton = eventautomatonmodel_automaton;
    }
    public List<EventAutomatonModel_AbstractTransition> getEventautomatonmodel_abstracttransitions() {
        return eventautomatonmodel_abstracttransitions;
    }

    public void addEventautomatonmodel_abstracttransition(Eventautomatonmodel_abstracttransition eventautomatonmodel_abstracttransition) {
        this.eventautomatonmodel_abstracttransitions.add(eventautomatonmodel_abstracttransition);
    }
    public EventAutomatonModel_AbstractTransition getEventautomatonmodel_abstracttransition() {
        return eventautomatonmodel_abstracttransition;
    }

    public void setEventautomatonmodel_abstracttransition(EventAutomatonModel_AbstractTransition eventautomatonmodel_abstracttransition) {
        this.eventautomatonmodel_abstracttransition = eventautomatonmodel_abstracttransition;
    }
    public List<EventAutomatonModel_Token> getEventautomatonmodel_tokens() {
        return eventautomatonmodel_tokens;
    }

    public void addEventautomatonmodel_token(Eventautomatonmodel_token eventautomatonmodel_token) {
        this.eventautomatonmodel_tokens.add(eventautomatonmodel_token);
    }
    public EventAutomatonModel_Automaton getEventautomatonmodel_automaton() {
        return eventautomatonmodel_automaton;
    }

    public void setEventautomatonmodel_automaton(EventAutomatonModel_Automaton eventautomatonmodel_automaton) {
        this.eventautomatonmodel_automaton = eventautomatonmodel_automaton;
    }

}