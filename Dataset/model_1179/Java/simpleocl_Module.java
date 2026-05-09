





import java.util.List;
import java.util.ArrayList;

public class simpleocl_Module extends NamedElement {






    private List<simpleocl_ModuleElement> simpleocl_moduleelements;




    private simpleocl_ModuleElement simpleocl_moduleelement;


    public simpleocl_Module(
    ) {
        super(
        );
        this.simpleocl_moduleelements = new ArrayList<>();
    }

    public simpleocl_Module(
        ArrayList<simpleocl_ModuleElement> simpleocl_moduleelements    ) {
        this.simpleocl_moduleelements = simpleocl_moduleelements;
    }


    public List<simpleocl_ModuleElement> getSimpleocl_moduleelements() {
        return simpleocl_moduleelements;
    }

    public void addSimpleocl_moduleelement(Simpleocl_moduleelement simpleocl_moduleelement) {
        this.simpleocl_moduleelements.add(simpleocl_moduleelement);
    }
    public simpleocl_ModuleElement getSimpleocl_moduleelement() {
        return simpleocl_moduleelement;
    }

    public void setSimpleocl_moduleelement(simpleocl_ModuleElement simpleocl_moduleelement) {
        this.simpleocl_moduleelement = simpleocl_moduleelement;
    }

}