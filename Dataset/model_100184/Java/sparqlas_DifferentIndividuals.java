





import java.util.List;
import java.util.ArrayList;

public class sparqlas_DifferentIndividuals extends Assertion {






    private List<sparqlas_Individual> sparqlas_individuals;


    public sparqlas_DifferentIndividuals(
    ) {
        super(
        );
        this.sparqlas_individuals = new ArrayList<>();
    }

    public sparqlas_DifferentIndividuals(
        ArrayList<sparqlas_Individual> sparqlas_individuals    ) {
        this.sparqlas_individuals = sparqlas_individuals;
    }


    public List<sparqlas_Individual> getSparqlas_individuals() {
        return sparqlas_individuals;
    }

    public void addSparqlas_individual(Sparqlas_individual sparqlas_individual) {
        this.sparqlas_individuals.add(sparqlas_individual);
    }

}