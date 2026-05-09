





import java.util.List;
import java.util.ArrayList;

public class uma_CustomCategory extends ContentCategory {

    private String group2;
    private String categorizedElement;
    private String subCategory;



    public uma_CustomCategory(
        String group2,        String categorizedElement,        String subCategory    ) {
        super(
        );
        this.group2 = group2;
        this.categorizedElement = categorizedElement;
        this.subCategory = subCategory;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getCategorizedelement() {
        return categorizedElement;
    }

    public void setCategorizedelement(String categorizedElement) {
        this.categorizedElement = categorizedElement;
    }
    public String getSubcategory() {
        return subCategory;
    }

    public void setSubcategory(String subCategory) {
        this.subCategory = subCategory;
    }


}