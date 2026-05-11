





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_TransitionFeature  {

    private String name;





    private fuzzyAutomaton_Transition fuzzyautomaton_transition;




    private fuzzyAutomaton_FuzzyAutomaton fuzzyautomaton_fuzzyautomaton;




    private List<fuzzyAutomaton_Transition> fuzzyautomaton_transitions;


    public fuzzyAutomaton_TransitionFeature(
        String name    ) {
        this.name = name;
        this.fuzzyautomaton_transitions = new ArrayList<>();
    }

    public fuzzyAutomaton_TransitionFeature(
        String name        ArrayList<fuzzyAutomaton_Transition> fuzzyautomaton_transitions    ) {
        this.name = name;
        this.fuzzyautomaton_transitions = fuzzyautomaton_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fuzzyAutomaton_Transition getFuzzyautomaton_transition() {
        return fuzzyautomaton_transition;
    }

    public void setFuzzyautomaton_transition(fuzzyAutomaton_Transition fuzzyautomaton_transition) {
        this.fuzzyautomaton_transition = fuzzyautomaton_transition;
    }
    public fuzzyAutomaton_FuzzyAutomaton getFuzzyautomaton_fuzzyautomaton() {
        return fuzzyautomaton_fuzzyautomaton;
    }

    public void setFuzzyautomaton_fuzzyautomaton(fuzzyAutomaton_FuzzyAutomaton fuzzyautomaton_fuzzyautomaton) {
        this.fuzzyautomaton_fuzzyautomaton = fuzzyautomaton_fuzzyautomaton;
    }
    public List<fuzzyAutomaton_Transition> getFuzzyautomaton_transitions() {
        return fuzzyautomaton_transitions;
    }

    public void addFuzzyautomaton_transition(Fuzzyautomaton_transition fuzzyautomaton_transition) {
        this.fuzzyautomaton_transitions.add(fuzzyautomaton_transition);
    }

}