





import java.util.List;
import java.util.ArrayList;

public class edu_Loop extends Statement {






    private List<edu_Invariant> edu_invariants;




    private edu_Block edu_block;




    private edu_Expression edu_expression;


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
    public edu_Block getEdu_block() {
        return edu_block;
    }

    public void setEdu_block(edu_Block edu_block) {
        this.edu_block = edu_block;
    }
    public edu_Expression getEdu_expression() {
        return edu_expression;
    }

    public void setEdu_expression(edu_Expression edu_expression) {
        this.edu_expression = edu_expression;
    }

}