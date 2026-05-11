





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentPrototypeBinding extends PrototypeBinding {






    private List<aadl2_ComponentPrototypeActual> aadl2_componentprototypeactuals;


    public aadl2_ComponentPrototypeBinding(
    ) {
        super(
        );
        this.aadl2_componentprototypeactuals = new ArrayList<>();
    }

    public aadl2_ComponentPrototypeBinding(
        ArrayList<aadl2_ComponentPrototypeActual> aadl2_componentprototypeactuals    ) {
        this.aadl2_componentprototypeactuals = aadl2_componentprototypeactuals;
    }


    public List<aadl2_ComponentPrototypeActual> getAadl2_componentprototypeactuals() {
        return aadl2_componentprototypeactuals;
    }

    public void addAadl2_componentprototypeactual(Aadl2_componentprototypeactual aadl2_componentprototypeactual) {
        this.aadl2_componentprototypeactuals.add(aadl2_componentprototypeactual);
    }

}