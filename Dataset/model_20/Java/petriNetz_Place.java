





import java.util.List;
import java.util.ArrayList;

public class petriNetz_Place  {

    private String name;





    private petriNetz_PTArc petrinetz_ptarc;




    private petriNetz_TPArc petrinetz_tparc;




    private petriNetz_Petrinet petrinetz_petrinet;




    private List<petriNetz_TPArc> petrinetz_tparcs;




    private List<petriNetz_PTArc> petrinetz_ptarcs;


    public petriNetz_Place(
        String name    ) {
        this.name = name;
        this.petrinetz_tparcs = new ArrayList<>();
        this.petrinetz_ptarcs = new ArrayList<>();
    }

    public petriNetz_Place(
        String name        ArrayList<petriNetz_TPArc> petrinetz_tparcs,        ArrayList<petriNetz_PTArc> petrinetz_ptarcs    ) {
        this.name = name;
        this.petrinetz_tparcs = petrinetz_tparcs;
        this.petrinetz_ptarcs = petrinetz_ptarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petriNetz_PTArc getPetrinetz_ptarc() {
        return petrinetz_ptarc;
    }

    public void setPetrinetz_ptarc(petriNetz_PTArc petrinetz_ptarc) {
        this.petrinetz_ptarc = petrinetz_ptarc;
    }
    public petriNetz_TPArc getPetrinetz_tparc() {
        return petrinetz_tparc;
    }

    public void setPetrinetz_tparc(petriNetz_TPArc petrinetz_tparc) {
        this.petrinetz_tparc = petrinetz_tparc;
    }
    public petriNetz_Petrinet getPetrinetz_petrinet() {
        return petrinetz_petrinet;
    }

    public void setPetrinetz_petrinet(petriNetz_Petrinet petrinetz_petrinet) {
        this.petrinetz_petrinet = petrinetz_petrinet;
    }
    public List<petriNetz_TPArc> getPetrinetz_tparcs() {
        return petrinetz_tparcs;
    }

    public void addPetrinetz_tparc(Petrinetz_tparc petrinetz_tparc) {
        this.petrinetz_tparcs.add(petrinetz_tparc);
    }
    public List<petriNetz_PTArc> getPetrinetz_ptarcs() {
        return petrinetz_ptarcs;
    }

    public void addPetrinetz_ptarc(Petrinetz_ptarc petrinetz_ptarc) {
        this.petrinetz_ptarcs.add(petrinetz_ptarc);
    }

}