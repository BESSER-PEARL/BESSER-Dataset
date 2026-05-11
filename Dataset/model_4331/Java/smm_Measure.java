





import java.util.List;
import java.util.ArrayList;

public class smm_Measure extends SmmElement {

    private String library;
    private String name;





    private smm_Category smm_category;




    private smm_MeasureRelationship smm_measurerelationship;




    private smm_MeasureRelationship smm_measurerelationship;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private List<smm_Category> smm_categorys;




    private List<smm_Measure> smm_measures;




    private smm_Measure smm_measure;




    private smm_Measure smm_measure;




    private List<smm_MeasureRelationship> smm_measurerelationships;


    public smm_Measure(
        String library,        String name    ) {
        super(
        );
        this.library = library;
        this.name = name;
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_categorys = new ArrayList<>();
        this.smm_measures = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
    }

    public smm_Measure(
        String library,        String name        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_Category> smm_categorys,        ArrayList<smm_Measure> smm_measures,        ArrayList<smm_MeasureRelationship> smm_measurerelationships    ) {
        this.library = library;
        this.name = name;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_categorys = smm_categorys;
        this.smm_measures = smm_measures;
        this.smm_measurerelationships = smm_measurerelationships;
    }

    public String getLibrary() {
        return library;
    }

    public void setLibrary(String library) {
        this.library = library;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smm_Category getSmm_category() {
        return smm_category;
    }

    public void setSmm_category(smm_Category smm_category) {
        this.smm_category = smm_category;
    }
    public smm_MeasureRelationship getSmm_measurerelationship() {
        return smm_measurerelationship;
    }

    public void setSmm_measurerelationship(smm_MeasureRelationship smm_measurerelationship) {
        this.smm_measurerelationship = smm_measurerelationship;
    }
    public smm_MeasureRelationship getSmm_measurerelationship() {
        return smm_measurerelationship;
    }

    public void setSmm_measurerelationship(smm_MeasureRelationship smm_measurerelationship) {
        this.smm_measurerelationship = smm_measurerelationship;
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
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
    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }
    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }

}