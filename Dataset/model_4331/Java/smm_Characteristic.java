





import java.util.List;
import java.util.ArrayList;

public class smm_Characteristic extends SmmElement {

    private String name;





    private smm_Measure smm_measure;




    private smm_Characteristic smm_characteristic;




    private List<smm_Measure> smm_measures;


    public smm_Characteristic(
        String name    ) {
        super(
        );
        this.name = name;
        this.smm_measures = new ArrayList<>();
    }

    public smm_Characteristic(
        String name        ArrayList<smm_Measure> smm_measures    ) {
        this.name = name;
        this.smm_measures = smm_measures;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }
    public smm_Characteristic getSmm_characteristic() {
        return smm_characteristic;
    }

    public void setSmm_characteristic(smm_Characteristic smm_characteristic) {
        this.smm_characteristic = smm_characteristic;
    }
    public List<smm_Measure> getSmm_measures() {
        return smm_measures;
    }

    public void addSmm_measure(Smm_measure smm_measure) {
        this.smm_measures.add(smm_measure);
    }

}