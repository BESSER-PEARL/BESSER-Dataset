





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OclModel extends NamedElement {






    private List<simpleocl_OclModelElement> simpleocl_oclmodelelements;




    private simpleocl_OclModelElementExp simpleocl_oclmodelelementexp;




    private simpleocl_OclModelElement simpleocl_oclmodelelement;


    public simpleocl_OclModel(
    ) {
        super(
        );
        this.simpleocl_oclmodelelements = new ArrayList<>();
    }

    public simpleocl_OclModel(
        ArrayList<simpleocl_OclModelElement> simpleocl_oclmodelelements    ) {
        this.simpleocl_oclmodelelements = simpleocl_oclmodelelements;
    }


    public List<simpleocl_OclModelElement> getSimpleocl_oclmodelelements() {
        return simpleocl_oclmodelelements;
    }

    public void addSimpleocl_oclmodelelement(Simpleocl_oclmodelelement simpleocl_oclmodelelement) {
        this.simpleocl_oclmodelelements.add(simpleocl_oclmodelelement);
    }
    public simpleocl_OclModelElementExp getSimpleocl_oclmodelelementexp() {
        return simpleocl_oclmodelelementexp;
    }

    public void setSimpleocl_oclmodelelementexp(simpleocl_OclModelElementExp simpleocl_oclmodelelementexp) {
        this.simpleocl_oclmodelelementexp = simpleocl_oclmodelelementexp;
    }
    public simpleocl_OclModelElement getSimpleocl_oclmodelelement() {
        return simpleocl_oclmodelelement;
    }

    public void setSimpleocl_oclmodelelement(simpleocl_OclModelElement simpleocl_oclmodelelement) {
        this.simpleocl_oclmodelelement = simpleocl_oclmodelelement;
    }

}