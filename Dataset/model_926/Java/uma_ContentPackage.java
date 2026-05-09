





import java.util.List;
import java.util.ArrayList;

public class uma_ContentPackage extends MethodPackage {






    private List<uma_ContentElement> uma_contentelements;


    public uma_ContentPackage(
    ) {
        super(
        );
        this.uma_contentelements = new ArrayList<>();
    }

    public uma_ContentPackage(
        ArrayList<uma_ContentElement> uma_contentelements    ) {
        this.uma_contentelements = uma_contentelements;
    }


    public List<uma_ContentElement> getUma_contentelements() {
        return uma_contentelements;
    }

    public void addUma_contentelement(Uma_contentelement uma_contentelement) {
        this.uma_contentelements.add(uma_contentelement);
    }

}