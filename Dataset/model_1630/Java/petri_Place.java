





import java.util.List;
import java.util.ArrayList;

public class petri_Place  {

    private String name;
    private int tokens;





    private petri_RedPetri petri_redpetri;




    private petri_Transition petri_transition;




    private List<petri_Transition> petri_transitions;


    public petri_Place(
        String name,        int tokens    ) {
        this.name = name;
        this.tokens = tokens;
        this.petri_transitions = new ArrayList<>();
    }

    public petri_Place(
        String name,        int tokens        ArrayList<petri_Transition> petri_transitions    ) {
        this.name = name;
        this.tokens = tokens;
        this.petri_transitions = petri_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }

    public petri_RedPetri getPetri_redpetri() {
        return petri_redpetri;
    }

    public void setPetri_redpetri(petri_RedPetri petri_redpetri) {
        this.petri_redpetri = petri_redpetri;
    }
    public petri_Transition getPetri_transition() {
        return petri_transition;
    }

    public void setPetri_transition(petri_Transition petri_transition) {
        this.petri_transition = petri_transition;
    }
    public List<petri_Transition> getPetri_transitions() {
        return petri_transitions;
    }

    public void addPetri_transition(Petri_transition petri_transition) {
        this.petri_transitions.add(petri_transition);
    }

}