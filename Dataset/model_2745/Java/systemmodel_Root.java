





import java.util.List;
import java.util.ArrayList;

public class systemmodel_Root extends SMElement {






    private List<systemmodel_ModelElement> systemmodel_modelelements;


    public systemmodel_Root(
    ) {
        super(
        );
        this.systemmodel_modelelements = new ArrayList<>();
    }

    public systemmodel_Root(
        ArrayList<systemmodel_ModelElement> systemmodel_modelelements    ) {
        this.systemmodel_modelelements = systemmodel_modelelements;
    }


    public List<systemmodel_ModelElement> getSystemmodel_modelelements() {
        return systemmodel_modelelements;
    }

    public void addSystemmodel_modelelement(Systemmodel_modelelement systemmodel_modelelement) {
        this.systemmodel_modelelements.add(systemmodel_modelelement);
    }

}