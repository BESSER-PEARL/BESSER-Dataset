





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_OrDep extends Dependence {






    private mancoosimm_Dependence mancoosimm_dependence;




    private mancoosimm_Dependence mancoosimm_dependence;




    private List<mancoosimm_Dependence> mancoosimm_dependences;


    public mancoosimm_OrDep(
    ) {
        super(
        );
        this.mancoosimm_dependences = new ArrayList<>();
    }

    public mancoosimm_OrDep(
        ArrayList<mancoosimm_Dependence> mancoosimm_dependences    ) {
        this.mancoosimm_dependences = mancoosimm_dependences;
    }


    public mancoosimm_Dependence getMancoosimm_dependence() {
        return mancoosimm_dependence;
    }

    public void setMancoosimm_dependence(mancoosimm_Dependence mancoosimm_dependence) {
        this.mancoosimm_dependence = mancoosimm_dependence;
    }
    public mancoosimm_Dependence getMancoosimm_dependence() {
        return mancoosimm_dependence;
    }

    public void setMancoosimm_dependence(mancoosimm_Dependence mancoosimm_dependence) {
        this.mancoosimm_dependence = mancoosimm_dependence;
    }
    public List<mancoosimm_Dependence> getMancoosimm_dependences() {
        return mancoosimm_dependences;
    }

    public void addMancoosimm_dependence(Mancoosimm_dependence mancoosimm_dependence) {
        this.mancoosimm_dependences.add(mancoosimm_dependence);
    }

}