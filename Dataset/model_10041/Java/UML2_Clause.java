





import java.util.List;
import java.util.ArrayList;

public class UML2_Clause extends Element {






    private List<UML2_Clause> uml2_clauses;




    private UML2_Clause uml2_clause;


    public UML2_Clause(
    ) {
        super(
        );
        this.uml2_clauses = new ArrayList<>();
    }

    public UML2_Clause(
        ArrayList<UML2_Clause> uml2_clauses    ) {
        this.uml2_clauses = uml2_clauses;
    }


    public List<UML2_Clause> getUml2_clauses() {
        return uml2_clauses;
    }

    public void addUml2_clause(Uml2_clause uml2_clause) {
        this.uml2_clauses.add(uml2_clause);
    }
    public UML2_Clause getUml2_clause() {
        return uml2_clause;
    }

    public void setUml2_clause(UML2_Clause uml2_clause) {
        this.uml2_clause = uml2_clause;
    }

}