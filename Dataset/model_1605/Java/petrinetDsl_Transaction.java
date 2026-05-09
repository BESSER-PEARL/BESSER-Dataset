





import java.util.List;
import java.util.ArrayList;

public class petrinetDsl_Transaction  {

    private String name;





    private petrinetDsl_PetriNet petrinetdsl_petrinet;


    public petrinetDsl_Transaction(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinetDsl_PetriNet getPetrinetdsl_petrinet() {
        return petrinetdsl_petrinet;
    }

    public void setPetrinetdsl_petrinet(petrinetDsl_PetriNet petrinetdsl_petrinet) {
        this.petrinetdsl_petrinet = petrinetdsl_petrinet;
    }

}