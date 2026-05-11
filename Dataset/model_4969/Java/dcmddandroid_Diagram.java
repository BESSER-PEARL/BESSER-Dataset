





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_Diagram extends NamedElement {






    private List<dcmddandroid_ModelElement> dcmddandroid_modelelements;


    public dcmddandroid_Diagram(
    ) {
        super(
        );
        this.dcmddandroid_modelelements = new ArrayList<>();
    }

    public dcmddandroid_Diagram(
        ArrayList<dcmddandroid_ModelElement> dcmddandroid_modelelements    ) {
        this.dcmddandroid_modelelements = dcmddandroid_modelelements;
    }


    public List<dcmddandroid_ModelElement> getDcmddandroid_modelelements() {
        return dcmddandroid_modelelements;
    }

    public void addDcmddandroid_modelelement(Dcmddandroid_modelelement dcmddandroid_modelelement) {
        this.dcmddandroid_modelelements.add(dcmddandroid_modelelement);
    }

}