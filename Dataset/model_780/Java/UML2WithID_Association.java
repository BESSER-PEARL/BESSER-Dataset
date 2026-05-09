





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Association extends Classifier, Element {






    private List<UML2WithID_Property> uml2withid_propertys;


    public UML2WithID_Association(
    ) {
        super(
        );
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_Association(
        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.uml2withid_propertys = uml2withid_propertys;
    }


    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }

}