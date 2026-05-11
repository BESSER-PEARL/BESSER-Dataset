





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_FuzzyConstraint  {

    private String tNorm;
    private String name;





    private fuzzyAutomaton_TransitionFeature fuzzyautomaton_transitionfeature;


    public fuzzyAutomaton_FuzzyConstraint(
        String tNorm,        String name    ) {
        this.tNorm = tNorm;
        this.name = name;
    }


    public String getTnorm() {
        return tNorm;
    }

    public void setTnorm(String tNorm) {
        this.tNorm = tNorm;
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