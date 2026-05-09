





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Clause extends Element {






    private List<UML2WithID_Clause> uml2withid_clauses;




    private UML2WithID_Clause uml2withid_clause;


    public UML2WithID_Clause(
    ) {
        super(
        );
        this.uml2withid_clauses = new ArrayList<>();
    }

    public UML2WithID_Clause(
        ArrayList<UML2WithID_Clause> uml2withid_clauses    ) {
        this.uml2withid_clauses = uml2withid_clauses;
    }


    public List<UML2WithID_Clause> getUml2withid_clauses() {
        return uml2withid_clauses;
    }

    public void addUml2withid_clause(Uml2withid_clause uml2withid_clause) {
        this.uml2withid_clauses.add(uml2withid_clause);
    }
    public UML2WithID_Clause getUml2withid_clause() {
        return uml2withid_clause;
    }

    public void setUml2withid_clause(UML2WithID_Clause uml2withid_clause) {
        this.uml2withid_clause = uml2withid_clause;
    }

}