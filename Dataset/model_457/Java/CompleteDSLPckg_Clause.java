





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Clause extends Element {






    private List<CompleteDSLPckg_Clause> completedslpckg_clauses;




    private CompleteDSLPckg_Clause completedslpckg_clause;


    public CompleteDSLPckg_Clause(
    ) {
        super(
        );
        this.completedslpckg_clauses = new ArrayList<>();
    }

    public CompleteDSLPckg_Clause(
        ArrayList<CompleteDSLPckg_Clause> completedslpckg_clauses    ) {
        this.completedslpckg_clauses = completedslpckg_clauses;
    }


    public List<CompleteDSLPckg_Clause> getCompletedslpckg_clauses() {
        return completedslpckg_clauses;
    }

    public void addCompletedslpckg_clause(Completedslpckg_clause completedslpckg_clause) {
        this.completedslpckg_clauses.add(completedslpckg_clause);
    }
    public CompleteDSLPckg_Clause getCompletedslpckg_clause() {
        return completedslpckg_clause;
    }

    public void setCompletedslpckg_clause(CompleteDSLPckg_Clause completedslpckg_clause) {
        this.completedslpckg_clause = completedslpckg_clause;
    }

}