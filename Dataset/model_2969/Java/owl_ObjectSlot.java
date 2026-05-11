





import java.util.List;
import java.util.ArrayList;

public class owl_ObjectSlot  {






    private List<owl_Individual> owl_individuals;




    private owl_OWLObjectProperty owl_owlobjectproperty;




    private owl_Individual owl_individual;




    private owl_Individual owl_individual;


    public owl_ObjectSlot(
    ) {
        this.owl_individuals = new ArrayList<>();
    }

    public owl_ObjectSlot(
        ArrayList<owl_Individual> owl_individuals    ) {
        this.owl_individuals = owl_individuals;
    }


    public List<owl_Individual> getOwl_individuals() {
        return owl_individuals;
    }

    public void addOwl_individual(Owl_individual owl_individual) {
        this.owl_individuals.add(owl_individual);
    }
    public owl_OWLObjectProperty getOwl_owlobjectproperty() {
        return owl_owlobjectproperty;
    }

    public void setOwl_owlobjectproperty(owl_OWLObjectProperty owl_owlobjectproperty) {
        this.owl_owlobjectproperty = owl_owlobjectproperty;
    }
    public owl_Individual getOwl_individual() {
        return owl_individual;
    }

    public void setOwl_individual(owl_Individual owl_individual) {
        this.owl_individual = owl_individual;
    }
    public owl_Individual getOwl_individual() {
        return owl_individual;
    }

    public void setOwl_individual(owl_Individual owl_individual) {
        this.owl_individual = owl_individual;
    }

}