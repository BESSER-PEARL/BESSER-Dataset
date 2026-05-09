





import java.util.List;
import java.util.ArrayList;

public class UML2_Property extends StructuralFeature, DeploymentTarget, ConnectableElement {






    private List<UML2_Property> uml2_propertys;


    public UML2_Property(
    ) {
        super(
        );
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        ArrayList<UML2_Property> uml2_propertys    ) {
        this.uml2_propertys = uml2_propertys;
    }


    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}