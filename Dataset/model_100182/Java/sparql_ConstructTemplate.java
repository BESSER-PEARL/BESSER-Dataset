





import java.util.List;
import java.util.ArrayList;

public class sparql_ConstructTemplate extends LocatedElement {






    private List<sparql_TriplesSameSubject> sparql_triplessamesubjects;


    public sparql_ConstructTemplate(
    ) {
        super(
        );
        this.sparql_triplessamesubjects = new ArrayList<>();
    }

    public sparql_ConstructTemplate(
        ArrayList<sparql_TriplesSameSubject> sparql_triplessamesubjects    ) {
        this.sparql_triplessamesubjects = sparql_triplessamesubjects;
    }


    public List<sparql_TriplesSameSubject> getSparql_triplessamesubjects() {
        return sparql_triplessamesubjects;
    }

    public void addSparql_triplessamesubject(Sparql_triplessamesubject sparql_triplessamesubject) {
        this.sparql_triplessamesubjects.add(sparql_triplessamesubject);
    }

}