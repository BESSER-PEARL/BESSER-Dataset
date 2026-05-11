





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_VarTransformation  {

    private String name;





    private fuzzyAutomaton_TransitionFeature fuzzyautomaton_transitionfeature;


    public fuzzyAutomaton_VarTransformation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fuzzyAutomaton_TransitionFeature getFuzzyautomaton_transitionfeature() {
        return fuzzyautomaton_transitionfeature;
    }

    public void setFuzzyautomaton_transitionfeature(fuzzyAutomaton_TransitionFeature fuzzyautomaton_transitionfeature) {
        this.fuzzyautomaton_transitionfeature = fuzzyautomaton_transitionfeature;
    }

}