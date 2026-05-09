





import java.util.List;
import java.util.ArrayList;

public class ea_automata_Automaton extends ExtendibleElement {

    private String usedExtensionIds;
    private String id;
    private String name;





    private Module module;




    private List<Transition> transitions;


    public ea_automata_Automaton(
        String usedExtensionIds,        String id,        String name    ) {
        super(
        );
        this.usedExtensionIds = usedExtensionIds;
        this.id = id;
        this.name = name;
        this.transitions = new ArrayList<>();
    }

    public ea_automata_Automaton(
        String usedExtensionIds,        String id,        String name        ArrayList<Transition> transitions    ) {
        this.usedExtensionIds = usedExtensionIds;
        this.id = id;
        this.name = name;
        this.transitions = transitions;
    }

    public String getUsedextensionids() {
        return usedExtensionIds;
    }

    public void setUsedextensionids(String usedExtensionIds) {
        this.usedExtensionIds = usedExtensionIds;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Module getModule() {
        return module;
    }

    public void setModule(Module module) {
        this.module = module;
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}