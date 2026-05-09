





import java.util.List;
import java.util.ArrayList;

public class uma_CustomCategory extends ContentCategory {






    private List<uma_DescribableElement> uma_describableelements;


    public uma_CustomCategory(
    ) {
        super(
        );
        this.uma_describableelements = new ArrayList<>();
    }

    public uma_CustomCategory(
        ArrayList<uma_DescribableElement> uma_describableelements    ) {
        this.uma_describableelements = uma_describableelements;
    }


    public List<uma_DescribableElement> getUma_describableelements() {
        return uma_describableelements;
    }

    public void addUma_describableelement(Uma_describableelement uma_describableelement) {
        this.uma_describableelements.add(uma_describableelement);
    }

}