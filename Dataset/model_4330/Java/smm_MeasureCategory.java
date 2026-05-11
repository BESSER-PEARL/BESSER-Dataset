





import java.util.List;
import java.util.ArrayList;

public class smm_MeasureCategory extends AbstractMeasureElement {






    private smm_CategoryRelationship smm_categoryrelationship;




    private smm_MeasureCategory smm_measurecategory;




    private List<smm_MeasureCategory> smm_measurecategorys;


    public smm_MeasureCategory(
    ) {
        super(
        );
        this.smm_measurecategorys = new ArrayList<>();
    }

    public smm_MeasureCategory(
        ArrayList<smm_MeasureCategory> smm_measurecategorys    ) {
        this.smm_measurecategorys = smm_measurecategorys;
    }


    public smm_CategoryRelationship getSmm_categoryrelationship() {
        return smm_categoryrelationship;
    }

    public void setSmm_categoryrelationship(smm_CategoryRelationship smm_categoryrelationship) {
        this.smm_categoryrelationship = smm_categoryrelationship;
    }
    public smm_MeasureCategory getSmm_measurecategory() {
        return smm_measurecategory;
    }

    public void setSmm_measurecategory(smm_MeasureCategory smm_measurecategory) {
        this.smm_measurecategory = smm_measurecategory;
    }
    public List<smm_MeasureCategory> getSmm_measurecategorys() {
        return smm_measurecategorys;
    }

    public void addSmm_measurecategory(Smm_measurecategory smm_measurecategory) {
        this.smm_measurecategorys.add(smm_measurecategory);
    }

}