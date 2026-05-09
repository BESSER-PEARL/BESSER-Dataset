





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;
    private int token;





    private petrinet_Arc petrinet_arc;




    private List<petrinet_Transition> petrinet_transitions;




    private petrinet_PetriNet petrinet_petrinet;




    private petrinet_PetriNet petrinet_petrinet;


    public petrinet_Place(
        String name,        int token    ) {
        this.name = name;
        this.token = token;
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_Place(
        String name,        int token        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.name = name;
        this.token = token;
        this.petrinet_transitions = petrinet_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }

    public petrinet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(petrinet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}