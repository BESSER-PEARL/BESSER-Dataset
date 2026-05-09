





import java.util.List;
import java.util.ArrayList;

public class PetrinetDSL_Petrinet  {

    private String description;
    private String name;





    private PetrinetDSL_Petrinet petrinetdsl_petrinet;


    public PetrinetDSL_Petrinet(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetrinetDSL_Petrinet getPetrinetdsl_petrinet() {
        return petrinetdsl_petrinet;
    }

    public void setPetrinetdsl_petrinet(PetrinetDSL_Petrinet petrinetdsl_petrinet) {
        this.petrinetdsl_petrinet = petrinetdsl_petrinet;
    }

}