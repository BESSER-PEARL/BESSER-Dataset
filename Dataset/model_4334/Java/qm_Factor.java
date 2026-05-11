





import java.util.List;
import java.util.ArrayList;

public class qm_Factor extends CharacterizingElement {






    private List<qm_Factor> qm_factors;




    private qm_Factor qm_factor;


    public qm_Factor(
    ) {
        super(
        );
        this.qm_factors = new ArrayList<>();
    }

    public qm_Factor(
        ArrayList<qm_Factor> qm_factors    ) {
        this.qm_factors = qm_factors;
    }


    public List<qm_Factor> getQm_factors() {
        return qm_factors;
    }

    public void addQm_factor(Qm_factor qm_factor) {
        this.qm_factors.add(qm_factor);
    }
    public qm_Factor getQm_factor() {
        return qm_factor;
    }

    public void setQm_factor(qm_Factor qm_factor) {
        this.qm_factor = qm_factor;
    }

}