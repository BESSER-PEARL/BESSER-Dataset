





import java.util.List;
import java.util.ArrayList;

public class archimate_Principle extends MotivationElement {






    private List<archimate_Outcome> archimate_outcomes;


    public archimate_Principle(
    ) {
        super(
        );
        this.archimate_outcomes = new ArrayList<>();
    }

    public archimate_Principle(
        ArrayList<archimate_Outcome> archimate_outcomes    ) {
        this.archimate_outcomes = archimate_outcomes;
    }


    public List<archimate_Outcome> getArchimate_outcomes() {
        return archimate_outcomes;
    }

    public void addArchimate_outcome(Archimate_outcome archimate_outcome) {
        this.archimate_outcomes.add(archimate_outcome);
    }

}