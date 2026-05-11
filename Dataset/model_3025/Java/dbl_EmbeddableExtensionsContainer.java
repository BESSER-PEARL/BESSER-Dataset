





import java.util.List;
import java.util.ArrayList;

public class dbl_EmbeddableExtensionsContainer  {






    private List<dbl_ExtensibleElement> dbl_extensibleelements;


    public dbl_EmbeddableExtensionsContainer(
    ) {
        this.dbl_extensibleelements = new ArrayList<>();
    }

    public dbl_EmbeddableExtensionsContainer(
        ArrayList<dbl_ExtensibleElement> dbl_extensibleelements    ) {
        this.dbl_extensibleelements = dbl_extensibleelements;
    }


    public List<dbl_ExtensibleElement> getDbl_extensibleelements() {
        return dbl_extensibleelements;
    }

    public void addDbl_extensibleelement(Dbl_extensibleelement dbl_extensibleelement) {
        this.dbl_extensibleelements.add(dbl_extensibleelement);
    }

}