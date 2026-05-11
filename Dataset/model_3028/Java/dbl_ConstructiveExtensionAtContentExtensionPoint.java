





import java.util.List;
import java.util.ArrayList;

public class dbl_ConstructiveExtensionAtContentExtensionPoint  {






    private List<dbl_ConstructiveExtension> dbl_constructiveextensions;


    public dbl_ConstructiveExtensionAtContentExtensionPoint(
    ) {
        this.dbl_constructiveextensions = new ArrayList<>();
    }

    public dbl_ConstructiveExtensionAtContentExtensionPoint(
        ArrayList<dbl_ConstructiveExtension> dbl_constructiveextensions    ) {
        this.dbl_constructiveextensions = dbl_constructiveextensions;
    }


    public List<dbl_ConstructiveExtension> getDbl_constructiveextensions() {
        return dbl_constructiveextensions;
    }

    public void addDbl_constructiveextension(Dbl_constructiveextension dbl_constructiveextension) {
        this.dbl_constructiveextensions.add(dbl_constructiveextension);
    }

}