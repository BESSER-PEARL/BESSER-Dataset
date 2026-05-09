





import java.util.List;
import java.util.ArrayList;

public class umm_CodelistEntry  {

    private String description;
    private String name;





    private umm_Subset umm_subset;




    private umm_Original umm_original;


    public umm_CodelistEntry(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umm_Subset getUmm_subset() {
        return umm_subset;
    }

    public void setUmm_subset(umm_Subset umm_subset) {
        this.umm_subset = umm_subset;
    }
    public umm_Original getUmm_original() {
        return umm_original;
    }

    public void setUmm_original(umm_Original umm_original) {
        this.umm_original = umm_original;
    }

}