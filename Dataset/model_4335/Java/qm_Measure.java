





import java.util.List;
import java.util.ArrayList;

public class qm_Measure extends CharacterizingElement {

    private String type;





    private List<qm_Measure> qm_measures;




    private List<qm_Factor> qm_factors;


    public qm_Measure(
        String type    ) {
        super(
        );
        this.type = type;
        this.qm_measures = new ArrayList<>();
        this.qm_factors = new ArrayList<>();
    }

    public qm_Measure(
        String type        ArrayList<qm_Measure> qm_measures,        ArrayList<qm_Factor> qm_factors    ) {
        this.type = type;
        this.qm_measures = qm_measures;
        this.qm_factors = qm_factors;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<qm_Measure> getQm_measures() {
        return qm_measures;
    }

    public void addQm_measure(Qm_measure qm_measure) {
        this.qm_measures.add(qm_measure);
    }
    public List<qm_Factor> getQm_factors() {
        return qm_factors;
    }

    public void addQm_factor(Qm_factor qm_factor) {
        this.qm_factors.add(qm_factor);
    }

}