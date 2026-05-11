





import java.util.List;
import java.util.ArrayList;

public class smm_MeasureCategory extends AbstractMeasureElement {






    private smm_MeasureCategory smm_measurecategory;




    private List<smm_Measure> smm_measures;




    private smm_Measure smm_measure;




    private smm_MeasureCategory smm_measurecategory;


    public smm_MeasureCategory(
    ) {
        super(
        );
        this.smm_measures = new ArrayList<>();
    }

    public smm_MeasureCategory(
        ArrayList<smm_Measure> smm_measures    ) {
        this.smm_measures = smm_measures;
    }


    public smm_MeasureCategory getSmm_measurecategory() {
        return smm_measurecategory;
    }

    public void setSmm_measurecategory(smm_MeasureCategory smm_measurecategory) {
        this.smm_measurecategory = smm_measurecategory;
    }
    public List<smm_Measure> getSmm_measures() {
        return smm_measures;
    }

    public void addSmm_measure(Smm_measure smm_measure) {
        this.smm_measures.add(smm_measure);
    }
    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }
    public smm_MeasureCategory getSmm_measurecategory() {
        return smm_measurecategory;
    }

    public void setSmm_measurecategory(smm_MeasureCategory smm_measurecategory) {
        this.smm_measurecategory = smm_measurecategory;
    }

}