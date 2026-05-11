





import java.util.List;
import java.util.ArrayList;

public class edu_Loop extends Statement {






    private List<edu_Invariant> edu_invariants;


    public edu_Loop(
    ) {
        super(
        );
        this.edu_invariants = new ArrayList<>();
    }

    public edu_Loop(
        ArrayList<edu_Invariant> edu_invariants    ) {
        this.edu_invariants = edu_invariants;
    }


    public List<edu_Invariant> getEdu_invariants() {
        return edu_invariants;
    }

    public void addEdu_invariant(Edu_invariant edu_invariant) {
        this.edu_invariants.add(edu_invariant);
    }

}