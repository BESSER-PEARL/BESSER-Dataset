





import java.util.List;
import java.util.ArrayList;

public class sparql_PropertyListNotEmpty extends LocatedElement {






    private List<sparql_ObjectList> sparql_objectlists;




    private List<sparql_Verb> sparql_verbs;


    public sparql_PropertyListNotEmpty(
    ) {
        super(
        );
        this.sparql_objectlists = new ArrayList<>();
        this.sparql_verbs = new ArrayList<>();
    }

    public sparql_PropertyListNotEmpty(
        ArrayList<sparql_ObjectList> sparql_objectlists,        ArrayList<sparql_Verb> sparql_verbs    ) {
        this.sparql_objectlists = sparql_objectlists;
        this.sparql_verbs = sparql_verbs;
    }


    public List<sparql_ObjectList> getSparql_objectlists() {
        return sparql_objectlists;
    }

    public void addSparql_objectlist(Sparql_objectlist sparql_objectlist) {
        this.sparql_objectlists.add(sparql_objectlist);
    }
    public List<sparql_Verb> getSparql_verbs() {
        return sparql_verbs;
    }

    public void addSparql_verb(Sparql_verb sparql_verb) {
        this.sparql_verbs.add(sparql_verb);
    }

}