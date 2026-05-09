





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Clause extends Element {






    private uml3_0_0_Clause uml3_0_0_clause;




    private List<uml3_0_0_Clause> uml3_0_0_clauses;


    public uml3_0_0_Clause(
    ) {
        super(
        );
        this.uml3_0_0_clauses = new ArrayList<>();
    }

    public uml3_0_0_Clause(
        ArrayList<uml3_0_0_Clause> uml3_0_0_clauses    ) {
        this.uml3_0_0_clauses = uml3_0_0_clauses;
    }


    public uml3_0_0_Clause getUml3_0_0_clause() {
        return uml3_0_0_clause;
    }

    public void setUml3_0_0_clause(uml3_0_0_Clause uml3_0_0_clause) {
        this.uml3_0_0_clause = uml3_0_0_clause;
    }
    public List<uml3_0_0_Clause> getUml3_0_0_clauses() {
        return uml3_0_0_clauses;
    }

    public void addUml3_0_0_clause(Uml3_0_0_clause uml3_0_0_clause) {
        this.uml3_0_0_clauses.add(uml3_0_0_clause);
    }

}