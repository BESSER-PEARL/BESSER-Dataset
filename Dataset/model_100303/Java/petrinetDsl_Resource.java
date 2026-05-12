





import java.util.List;
import java.util.ArrayList;

public class petrinetDsl_Resource  {

    private String name;





    private petrinetDsl_PutStatement petrinetdsl_putstatement;




    private petrinetDsl_PetriNet petrinetdsl_petrinet;




    private petrinetDsl_TakeStatement petrinetdsl_takestatement;




    private petrinetDsl_AssureStatement petrinetdsl_assurestatement;


    public petrinetDsl_Resource(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinetDsl_PutStatement getPetrinetdsl_putstatement() {
        return petrinetdsl_putstatement;
    }

    public void setPetrinetdsl_putstatement(petrinetDsl_PutStatement petrinetdsl_putstatement) {
        this.petrinetdsl_putstatement = petrinetdsl_putstatement;
    }
    public petrinetDsl_PetriNet getPetrinetdsl_petrinet() {
        return petrinetdsl_petrinet;
    }

    public void setPetrinetdsl_petrinet(petrinetDsl_PetriNet petrinetdsl_petrinet) {
        this.petrinetdsl_petrinet = petrinetdsl_petrinet;
    }
    public petrinetDsl_TakeStatement getPetrinetdsl_takestatement() {
        return petrinetdsl_takestatement;
    }

    public void setPetrinetdsl_takestatement(petrinetDsl_TakeStatement petrinetdsl_takestatement) {
        this.petrinetdsl_takestatement = petrinetdsl_takestatement;
    }
    public petrinetDsl_AssureStatement getPetrinetdsl_assurestatement() {
        return petrinetdsl_assurestatement;
    }

    public void setPetrinetdsl_assurestatement(petrinetDsl_AssureStatement petrinetdsl_assurestatement) {
        this.petrinetdsl_assurestatement = petrinetdsl_assurestatement;
    }

}