





import java.util.List;
import java.util.ArrayList;

public class petrinetDsl_Transaction  {

    private String name;





    private petrinetDsl_PetriNet petrinetdsl_petrinet;




    private List<petrinetDsl_PutStatement> petrinetdsl_putstatements;




    private List<petrinetDsl_AssureStatement> petrinetdsl_assurestatements;




    private List<petrinetDsl_TakeStatement> petrinetdsl_takestatements;


    public petrinetDsl_Transaction(
        String name    ) {
        this.name = name;
        this.petrinetdsl_putstatements = new ArrayList<>();
        this.petrinetdsl_assurestatements = new ArrayList<>();
        this.petrinetdsl_takestatements = new ArrayList<>();
    }

    public petrinetDsl_Transaction(
        String name        ArrayList<petrinetDsl_PutStatement> petrinetdsl_putstatements,        ArrayList<petrinetDsl_AssureStatement> petrinetdsl_assurestatements,        ArrayList<petrinetDsl_TakeStatement> petrinetdsl_takestatements    ) {
        this.name = name;
        this.petrinetdsl_putstatements = petrinetdsl_putstatements;
        this.petrinetdsl_assurestatements = petrinetdsl_assurestatements;
        this.petrinetdsl_takestatements = petrinetdsl_takestatements;
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
    public List<petrinetDsl_PutStatement> getPetrinetdsl_putstatements() {
        return petrinetdsl_putstatements;
    }

    public void addPetrinetdsl_putstatement(Petrinetdsl_putstatement petrinetdsl_putstatement) {
        this.petrinetdsl_putstatements.add(petrinetdsl_putstatement);
    }
    public List<petrinetDsl_AssureStatement> getPetrinetdsl_assurestatements() {
        return petrinetdsl_assurestatements;
    }

    public void addPetrinetdsl_assurestatement(Petrinetdsl_assurestatement petrinetdsl_assurestatement) {
        this.petrinetdsl_assurestatements.add(petrinetdsl_assurestatement);
    }
    public List<petrinetDsl_TakeStatement> getPetrinetdsl_takestatements() {
        return petrinetdsl_takestatements;
    }

    public void addPetrinetdsl_takestatement(Petrinetdsl_takestatement petrinetdsl_takestatement) {
        this.petrinetdsl_takestatements.add(petrinetdsl_takestatement);
    }

}