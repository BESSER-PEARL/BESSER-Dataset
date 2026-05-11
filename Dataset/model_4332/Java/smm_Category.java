





import java.util.List;
import java.util.ArrayList;

public class smm_Category extends SmmElement {

    private String name;





    private List<smm_Category> smm_categorys;




    private List<smm_Measure> smm_measures;




    private smm_Category smm_category;




    private smm_Measure smm_measure;


    public smm_Category(
        String name    ) {
        super(
        );
        this.name = name;
        this.smm_categorys = new ArrayList<>();
        this.smm_measures = new ArrayList<>();
    }

    public smm_Category(
        String name        ArrayList<smm_Category> smm_categorys,        ArrayList<smm_Measure> smm_measures    ) {
        this.name = name;
        this.smm_categorys = smm_categorys;
        this.smm_measures = smm_measures;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<smm_Category> getSmm_categorys() {
        return smm_categorys;
    }

    public void addSmm_category(Smm_category smm_category) {
        this.smm_categorys.add(smm_category);
    }
    public List<smm_Measure> getSmm_measures() {
        return smm_measures;
    }

    public void addSmm_measure(Smm_measure smm_measure) {
        this.smm_measures.add(smm_measure);
    }
    public smm_Category getSmm_category() {
        return smm_category;
    }

    public void setSmm_category(smm_Category smm_category) {
        this.smm_category = smm_category;
    }
    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }

}