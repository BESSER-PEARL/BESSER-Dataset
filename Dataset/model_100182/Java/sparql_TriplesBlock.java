





import java.util.List;
import java.util.ArrayList;

public class sparql_TriplesBlock  {






    private sparql_AdditionalGGPElement sparql_additionalggpelement;




    private List<sparql_TriplesSameSubject> sparql_triplessamesubjects;




    private sparql_GroupGraphPattern sparql_groupgraphpattern;


    public sparql_TriplesBlock(
    ) {
        this.sparql_triplessamesubjects = new ArrayList<>();
    }

    public sparql_TriplesBlock(
        ArrayList<sparql_TriplesSameSubject> sparql_triplessamesubjects    ) {
        this.sparql_triplessamesubjects = sparql_triplessamesubjects;
    }


    public sparql_AdditionalGGPElement getSparql_additionalggpelement() {
        return sparql_additionalggpelement;
    }

    public void setSparql_additionalggpelement(sparql_AdditionalGGPElement sparql_additionalggpelement) {
        this.sparql_additionalggpelement = sparql_additionalggpelement;
    }
    public List<sparql_TriplesSameSubject> getSparql_triplessamesubjects() {
        return sparql_triplessamesubjects;
    }

    public void addSparql_triplessamesubject(Sparql_triplessamesubject sparql_triplessamesubject) {
        this.sparql_triplessamesubjects.add(sparql_triplessamesubject);
    }
    public sparql_GroupGraphPattern getSparql_groupgraphpattern() {
        return sparql_groupgraphpattern;
    }

    public void setSparql_groupgraphpattern(sparql_GroupGraphPattern sparql_groupgraphpattern) {
        this.sparql_groupgraphpattern = sparql_groupgraphpattern;
    }

}