





import java.util.List;
import java.util.ArrayList;

public class uma_CustomCategory extends ContentCategory {






    private List<uma_ContentCategory> uma_contentcategorys;




    private List<uma_DescribableElement> uma_describableelements;


    public uma_CustomCategory(
    ) {
        super(
        );
        this.uma_contentcategorys = new ArrayList<>();
        this.uma_describableelements = new ArrayList<>();
    }

    public uma_CustomCategory(
        ArrayList<uma_ContentCategory> uma_contentcategorys,        ArrayList<uma_DescribableElement> uma_describableelements    ) {
        this.uma_contentcategorys = uma_contentcategorys;
        this.uma_describableelements = uma_describableelements;
    }


    public List<uma_ContentCategory> getUma_contentcategorys() {
        return uma_contentcategorys;
    }

    public void addUma_contentcategory(Uma_contentcategory uma_contentcategory) {
        this.uma_contentcategorys.add(uma_contentcategory);
    }
    public List<uma_DescribableElement> getUma_describableelements() {
        return uma_describableelements;
    }

    public void addUma_describableelement(Uma_describableelement uma_describableelement) {
        this.uma_describableelements.add(uma_describableelement);
    }

}