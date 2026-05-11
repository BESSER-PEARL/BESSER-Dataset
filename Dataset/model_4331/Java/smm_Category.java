





import java.util.List;
import java.util.ArrayList;

public class smm_Category extends SmmElement {

    private String name;





    private smm_CategoryRelationship smm_categoryrelationship;




    private smm_Category smm_category;




    private List<smm_CategoryRelationship> smm_categoryrelationships;




    private List<smm_CategoryRelationship> smm_categoryrelationships;




    private List<smm_Category> smm_categorys;




    private smm_CategoryRelationship smm_categoryrelationship;


    public smm_Category(
        String name    ) {
        super(
        );
        this.name = name;
        this.smm_categoryrelationships = new ArrayList<>();
        this.smm_categoryrelationships = new ArrayList<>();
        this.smm_categorys = new ArrayList<>();
    }

    public smm_Category(
        String name        ArrayList<smm_CategoryRelationship> smm_categoryrelationships,        ArrayList<smm_CategoryRelationship> smm_categoryrelationships,        ArrayList<smm_Category> smm_categorys    ) {
        this.name = name;
        this.smm_categoryrelationships = smm_categoryrelationships;
        this.smm_categoryrelationships = smm_categoryrelationships;
        this.smm_categorys = smm_categorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smm_CategoryRelationship getSmm_categoryrelationship() {
        return smm_categoryrelationship;
    }

    public void setSmm_categoryrelationship(smm_CategoryRelationship smm_categoryrelationship) {
        this.smm_categoryrelationship = smm_categoryrelationship;
    }
    public smm_Category getSmm_category() {
        return smm_category;
    }

    public void setSmm_category(smm_Category smm_category) {
        this.smm_category = smm_category;
    }
    public List<smm_CategoryRelationship> getSmm_categoryrelationships() {
        return smm_categoryrelationships;
    }

    public void addSmm_categoryrelationship(Smm_categoryrelationship smm_categoryrelationship) {
        this.smm_categoryrelationships.add(smm_categoryrelationship);
    }
    public List<smm_CategoryRelationship> getSmm_categoryrelationships() {
        return smm_categoryrelationships;
    }

    public void addSmm_categoryrelationship(Smm_categoryrelationship smm_categoryrelationship) {
        this.smm_categoryrelationships.add(smm_categoryrelationship);
    }
    public List<smm_Category> getSmm_categorys() {
        return smm_categorys;
    }

    public void addSmm_category(Smm_category smm_category) {
        this.smm_categorys.add(smm_category);
    }
    public smm_CategoryRelationship getSmm_categoryrelationship() {
        return smm_categoryrelationship;
    }

    public void setSmm_categoryrelationship(smm_CategoryRelationship smm_categoryrelationship) {
        this.smm_categoryrelationship = smm_categoryrelationship;
    }

}