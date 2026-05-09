





import java.util.List;
import java.util.ArrayList;

public class uma_ContentCategoryPackage extends MethodPackage {

    private String group2;





    private List<uma_ContentCategory> uma_contentcategorys;


    public uma_ContentCategoryPackage(
        String group2    ) {
        super(
        );
        this.group2 = group2;
        this.uma_contentcategorys = new ArrayList<>();
    }

    public uma_ContentCategoryPackage(
        String group2        ArrayList<uma_ContentCategory> uma_contentcategorys    ) {
        this.group2 = group2;
        this.uma_contentcategorys = uma_contentcategorys;
    }

    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<uma_ContentCategory> getUma_contentcategorys() {
        return uma_contentcategorys;
    }

    public void addUma_contentcategory(Uma_contentcategory uma_contentcategory) {
        this.uma_contentcategorys.add(uma_contentcategory);
    }

}