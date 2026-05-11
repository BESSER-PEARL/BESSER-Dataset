





import java.util.List;
import java.util.ArrayList;

public class owl_OWLAllDifferent extends RDFSResource {






    private owl_Individual owl_individual;




    private List<owl_Individual> owl_individuals;


    public owl_OWLAllDifferent(
    ) {
        super(
        );
        this.owl_individuals = new ArrayList<>();
    }

    public owl_OWLAllDifferent(
        ArrayList<owl_Individual> owl_individuals    ) {
        this.owl_individuals = owl_individuals;
    }


    public owl_Individual getOwl_individual() {
        return owl_individual;
    }

    public void setOwl_individual(owl_Individual owl_individual) {
        this.owl_individual = owl_individual;
    }
    public List<owl_Individual> getOwl_individuals() {
        return owl_individuals;
    }

    public void addOwl_individual(Owl_individual owl_individual) {
        this.owl_individuals.add(owl_individual);
    }

}