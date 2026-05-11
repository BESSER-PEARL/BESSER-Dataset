





import java.util.List;
import java.util.ArrayList;

public class qm_Measure extends CharacterizingElement {

    private String type;





    private qm_Measure qm_measure;




    private List<qm_Factor> qm_factors;


    public qm_Measure(
        String type    ) {
        super(
        );
        this.type = type;
        this.qm_factors = new ArrayList<>();
    }

    public qm_Measure(
        String type        ArrayList<qm_Factor> qm_factors    ) {
        this.type = type;
        this.qm_factors = qm_factors;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public qm_Measure getQm_measure() {
        return qm_measure;
    }

    public void setQm_measure(qm_Measure qm_measure) {
        this.qm_measure = qm_measure;
    }
    public List<qm_Factor> getQm_factors() {
        return qm_factors;
    }

    public void addQm_factor(Qm_factor qm_factor) {
        this.qm_factors.add(qm_factor);
    }

}